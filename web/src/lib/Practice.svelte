<script lang="ts">
    import _ from "lodash";

    export let questions: {
        question: string;
        answer: string;
        question_image?: string;
        options: string[];
    }[];

    let current_question_index: number = _.random(questions.length);
    let attempted_questions_index: number[] = [];
    let score: number = 0;
    let current_correct_option: number | null = null;

    const getNextQuestion = () => {
        attempted_questions_index.push(current_question_index);
        questions.splice(current_question_index, 1);
        questions = questions;

        const question_index = _.random(questions.length - 1);

        console.log(
            attempted_questions_index,
            questions.length,
            question_index,
        );

        current_correct_option = null;
        current_question_index = question_index;

        attempted_questions_index = attempted_questions_index;
    };

    const computeScore = (selected_option_index: number) => {
        const current_question = questions[current_question_index];
        const answer_index = current_question.options.findIndex(
            (value) => value === current_question.answer,
        );

        if (current_correct_option === null)
            if (answer_index === selected_option_index) score += 1;

        current_correct_option = answer_index;
    };
</script>

<div class="flex flex-col h-full justify-evenly items-center w-full">
    {#if questions.length}
        <div class="flex flex-col justify-between gap-4 w-8/12">
            <div class="flex flex-row font-semibold gap-2">
                <div class="flex justify-center bg-gray-800 w-7 h-7 text-white">
                    {attempted_questions_index.length + 1}
                </div>
                <div class="">{questions[current_question_index].question}</div>
            </div>

            <div>
                {#if questions[current_question_index].question_image}
                    <img
                        src={questions[current_question_index].question_image}
                        alt=""
                        class="h-32 object-contain"
                    />
                {/if}
            </div>

            <div class="flex flex-col gap-2">
                {#each questions[current_question_index].options as option, idx}
                    {#if !option.startsWith("-")}
                        <button
                            class="flex flex-row text-left rounded-lg border hover:shadow-inner bg-white p-5 gap-4 transition-all duration-200"
                            class:bg-green-400={current_correct_option !==
                                null && current_correct_option === idx}
                            class:bg-red-400={current_correct_option !== null &&
                                current_correct_option !== idx}
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
            </div>

            <div class="flex justify-end">
                {#if current_correct_option !== null}
                    <button
                        class="border hover:shadow-inner p-2 px-4 rounded-lg"
                        on:click={getNextQuestion}>Next question</button
                    >
                {:else}
                    <span class="p-2 px-4"> &nbsp; </span>
                {/if}
            </div>
        </div>

        <div class="flex flex-col items-center">
            <p>
                {attempted_questions_index.length} of {questions.length +
                    attempted_questions_index.length} answered
            </p>
            <p>{score} correct</p>
        </div>
    {:else}
        <div>

            <!-- TODO: make final scores page -->

        </div>
    {/if}
</div>
