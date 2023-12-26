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
    })

</script>

<div class="flex flex-col justify-evenly items-center mt-10">
    <div class="flex flex-col w-8/12 gap-10">
        {#each questions as question, i}
            <div class="flex flex-col justify-between">
                <div class="flex flex-row font-semibold mb-5">
                    <div
                        class="flex justify-center bg-gray-800 w-7 h-7 text-white me-2"
                    >
                        {i + 1}
                    </div>
                    <div class="">{question.question}</div>
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

                <div class="flex flex-row h-16">
                    <div class="bg-green-500 h-full p-5">Answer:</div>
                    <div class=" bg-green-100 w-full ps-2 h-full pt-5">
                        {question.answer}
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>
