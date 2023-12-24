<script lang="ts">
    import { page } from "$app/stores";
    import Learn from "$lib/Learn.svelte";
    import Practice from "$lib/Practice.svelte";
    import {
        air_brake,
        class_five,
        class_five_new,
        class_one_new,
        class_one_semitruck,
    } from "../../../utils/questions";

    type categories =
        | "class1"
        | "class5"
        | "air brake"
        | "class 1 (semi-trailer truck)";

    type testMode = 'learn' | 'practice';

    $: testType = $page.params.type as testMode;
    $: category = $page.params.test as categories;

    const category_map = {
        class1: class_one_new,
        class5: class_five_new,
        "air brake": air_brake,
        "class 1 (semi-trailer truck)": class_one_semitruck,
    };

    $: curTest = category_map[category];
</script>

{#if testType === "learn"}
    <Learn bind:questions={curTest} />
{:else if testType === "practice"}
    <Practice bind:questions={curTest} />
{/if}
