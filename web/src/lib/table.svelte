<script lang="ts">
    import { goto } from "$app/navigation";

    export let heading = "default";
    export let slug: "learn" | "practice" = "learn";

    const pages = [
        "class1",
        "class5",
        "air brake",
        "class 1(semi-trailer truck)",
    ];

    let selectedPage = pages[0];

    const openSelectedPage = () => {
        if (selectedPage) {
            goto(`/${slug}/${selectedPage}`);
        }
    };

</script>

<div
    class="flex flex-col items-center justify-around border-solid border-2 border-sky-500 rounded h-80 w-80 m-4"
>
    <div>
        <h1 class="text-2xl font-bold">{heading}</h1>
    </div>
    <div>
        <div class=" pb-2">select category:</div>

        <select bind:value={selectedPage} class=" rounded-md bg-sky-100 p-2">
            {#each pages as page}
                <option value={page} selected={selectedPage === page}
                    >{page}</option
                >
            {/each}
        </select>
    </div>
    <button
        on:click={openSelectedPage}
        class="bg-sky-500 text-white px-4 py-2 rounded"
    >
        Start
    </button>
</div>
