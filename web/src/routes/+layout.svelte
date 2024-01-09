<script>
    import Footer from "$lib/Footer.svelte";
    import Header from "$lib/Header.svelte";
    import "../app.css";

    import { goto, invalidate } from "$app/navigation";
    import { onMount } from "svelte";

    export let data;
    let { supabase, session } = data;
    $: ({ supabase, session } = data);

    onMount(() => {
        const {
            data: { subscription },
        } = supabase.auth.onAuthStateChange((event, _session) => {
            if (_session?.expires_at !== session?.expires_at) {
                invalidate("supabase:auth");
            }
        });

        if (!session) {
            goto("/auth");
        }

        return () => subscription.unsubscribe();
    });
</script>

<svelte:head>
    <title>{import.meta.env.VITE_COMPANY_NAME}</title>
</svelte:head>

<Header bind:data />
<div class="h-screen flex flex-col justify-between pt-20">
    <slot />
    <div>
        <!-- <Footer /> -->
    </div>
</div>
