<script lang="ts">
    import _ from "lodash";
    import { onMount } from "svelte";

    export let questions: {
        question: string;
        answer: string;
        question_image?: string;
        options: string[];
    }[];

    onMount(() => {
        questions = _.shuffle(questions);
    });
</script>

<div class="flex flex-col justify-evenly items-center mt-10">
    <div class="flex flex-col w-8/12 gap-14">
        {#each questions as question, i}
            <div class="flex flex-col justify-between gap-4">
                <div class="flex flex-row font-semibold mb-5">
                    <div
                        class="flex justify-center bg-gray-800 w-7 h-7 text-white me-2"
                    >
                        {i + 1}
                    </div>
                    <div class="">{question.question}</div>
                </div>
                {#if question.question_image}
                    <div>
                        <img 
                            src="/question_images/{question.question_image}"
                            alt=""
                            class="h-32 object-contain"
                        />
                    </div>
                {/if}

                <div
                    class="flex flex-row text-left rounded-lg border hover:shadow-inner transition-all duration-200"
                >
                    <div class="bg-green-500 p-5 rounded-l-lg">Answer:</div>
                    <div class=" bg-green-100 p-5 w-full rounded-r-lg">
                        {question.answer}
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>
