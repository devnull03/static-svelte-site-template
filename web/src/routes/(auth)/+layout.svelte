<script lang="ts">
    import { onMount } from "svelte";

    import { goto } from "$app/navigation";

    export let data;
    let { supabase, session } = data;
    $: ({ supabase, session } = data);

    onMount(() => {
        if (session) {
            goto("/");
        }

    });

</script>


<slot />
