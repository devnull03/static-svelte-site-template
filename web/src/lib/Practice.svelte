<script lang="ts">
    import _ from "lodash";

    export let questions: {
        question: string;
        answer: string;
        question_image?: string;
        options: string[];
        selected?: number | null;
    }[];

    let questions_buffer: {
        question: string;
        answer: string;
        question_image?: string;
        options: string[];
        selected?: number | null;
    }[] = _.cloneDeep(questions);

    export let testName: string;

    let current_question_index: number = _.random(questions_buffer.length - 1);
    let attempted_questions: any[] = [];
    let score: number = 0;
    let current_correct_option: number | null = null;
    let current_selected_option: number | null = null;

    const getNextQuestion = () => {
        const q = questions_buffer[current_question_index];

        q.selected = current_selected_option;
        attempted_questions.push(q);

        questions_buffer.splice(current_question_index, 1);

        current_correct_option = null;
        current_selected_option = null;

        attempted_questions = attempted_questions;

        if (questions_buffer.length)
            current_question_index = _.random(0, questions_buffer.length - 1);
        else current_question_index = -1;

        questions_buffer = questions_buffer;
    };

    const computeScore = (selected_option_index: number) => {
        current_selected_option = selected_option_index;
        const current_question = questions_buffer[current_question_index];
        const answer_index = current_question.options.findIndex(
            (value) => value === current_question.answer,
        );

        if (current_correct_option === null)
            if (answer_index === selected_option_index) score += 1;

        current_correct_option = answer_index;
    };

    $: console.log(current_correct_option, current_selected_option);

    $: finalScore =
        (100 * score) / (questions_buffer.length + attempted_questions.length);
</script>

<div class="flex flex-col h-full items-center w-full">
    {#if current_question_index !== -1}
        <div class="flex flex-col justify-between gap-4 w-1/2">
            <div class="flex flex-row font-semibold gap-2">
                <div class="flex justify-center bg-gray-800 w-7 h-7 text-white">
                    {attempted_questions.length + 1}
                </div>
                <div class="">
                    {questions_buffer[current_question_index]?.question}
                </div>
            </div>

            <div>
                {#if questions_buffer[current_question_index]?.question_image}
                    <img
                        src={questions_buffer[current_question_index]
                            ?.question_image}
                        alt=""
                        class="h-32 object-contain"
                    />
                {/if}
            </div>

            <div class="flex flex-col gap-2">
                {#if questions_buffer.length}
                    {#each questions_buffer[current_question_index]?.options as option, idx}
                        {#if !option.startsWith("-")}
                            <button
                                class="flex flex-row text-left rounded-lg border hover:shadow-inner p-5 gap-4 transition-all duration-200"
                                class:bg-green-400={current_correct_option ===
                                    idx}
                                class:bg-red-400={current_selected_option ===
                                    idx && current_correct_option !== idx}
                                on:click={() => computeScore(idx)}
                                on:dblclick={() => {
                                    if (current_correct_option !== null)
                                        getNextQuestion();
                                }}
                            >
                                <div class="h-full">
                                    {["A", "B", "C", "D"][idx]}
                                </div>
                                <div class="w-full h-full">
                                    {option}
                                </div>
                            </button>
                        {/if}
                    {/each}
                {/if}
            </div>

            <div class="flex justify-end">
                {#if current_correct_option !== null && questions_buffer.length > 1}
                    <button
                        class="border hover:shadow-inner p-2 px-4 rounded-lg"
                        on:click={getNextQuestion}>Next question</button
                    >
                {:else if current_correct_option !== null && questions_buffer.length === 1}
                    <button
                        class="border hover:shadow-inner p-2 px-4 rounded-lg"
                        on:click={getNextQuestion}>Submit</button
                    >
                {:else}
                    <span class="p-2 px-4"> &nbsp; </span>
                {/if}
            </div>
        </div>

        <div class="flex flex-col items-center">
            <p>
                {attempted_questions.length} of {questions_buffer.length +
                    attempted_questions.length} answered
            </p>
            <p>{score} correct</p>
        </div>
    {:else}
        <div class="flex flex-col items-center gap-4 w-1/2">
            <p class="text-xl">
                {testName
                    .split(" ")
                    .map((e) => e[0].toUpperCase() + e.slice(1))
                    .join(" ")} test results
            </p>

            <p>
                Your score: <span
                    class="px-2 py-1 rounded-md"
                    class:bg-green-400={finalScore >= 80}
                    class:bg-orange-400={finalScore < 80 && finalScore >= 10}
                    class:bg-red-500={finalScore < 10}
                >
                    {finalScore}%
                </span>
            </p>

            <p>
                You got <span class="text-green-500">{score}</span> correct and
                <span class="text-orange-400">
                    {attempted_questions.length - score}</span
                > incorrect
            </p>

            {#if finalScore < 80}
                <p class="text-red-600">
                    A passing score of 80% is required on the real test
                </p>
            {/if}

            <button
                class="border rounded-lg p-2 px-4 hover:shadow-inner bg-gray-100 text-sm"
                on:click={async () => {
                    attempted_questions = [];
                    questions_buffer = _.cloneDeep(questions);
                    score = 0;
                    current_question_index = _.random(
                        questions_buffer.length - 1,
                    );
                }}>Try again</button
            >
            <hr class="w-1/2" />

            {#each attempted_questions as question, idxq}
                <div class="flex flex-col justify-between gap-4">
                    <div class="flex flex-row font-semibold gap-2">
                        <div
                            class="flex justify-center bg-gray-800 w-7 h-7 text-white"
                        >
                            {idxq + 1}
                        </div>
                        <div class="">
                            {question.question}
                        </div>
                    </div>

                    <div>
                        {#if question.question_image}
                            <img
                                src={question.question_image}
                                alt=""
                                class="h-32 object-contain"
                            />
                        {/if}
                    </div>

                    <div class="flex flex-col gap-2">
                        {#each question.options as option, idx}
                            {#if !option.startsWith("-")}
                                <button
                                    class="flex flex-row text-left rounded-lg border hover:shadow-inner bg-white p-5 gap-4 transition-all duration-200"
                                    class:bg-green-400={option ===
                                        question.answer}
                                    class:bg-red-400={question.selected ===
                                        idx && option !== question.answer}
                                >
                                    <div class="h-full">
                                        {["A", "B", "C", "D"][idx]}
                                    </div>
                                    <div class="w-full h-full">
                                        {option}
                                    </div>
                                </button>
                            {/if}
                        {/each}
                    </div>
                </div>
            {/each}
        </div>
    {/if}
</div>
