<script lang="ts">
    import { onMount } from "svelte";
    import { GoogleTranslate } from "@candidosales/svelte-google-translate";
    import type { Session, SupabaseClient } from "@supabase/supabase-js";
    import { goto } from "$app/navigation";
    import Loader from "./Loader.svelte";

    export let data: { supabase: SupabaseClient; session: Session | null };
    let { supabase, session } = data;
    $: ({ supabase, session } = data);

    const navLinks = [
        {
            name: "Home",
            href: "/",
        },
    ];

    let signoutLoading = false;

    const handleSignOut = async () => {
        signoutLoading = true;
        let res = await supabase.auth.signOut();
        setTimeout(() => {
            signoutLoading = false;
            goto("/auth");
        }, 200);
    };
</script>

<GoogleTranslate
    elementId={"google-translate-element"}
    options={{ pageLanguage: "en", includedLanguages: "pt,en,pa,hi,zh,tl,ja" }}
/>

<nav class="">
    <div
        class="top-0 bg-sky-500 h-20 w-full flex flex-row justify-between items-center fixed z-50"
    >
        <!-- top fixed -->
        <div class="flex text-white font-bold items-center ps-4">
            the driving school
        </div>

        <div class="flex flex-row justify-evenly gap-8 items-center pe-4">
            <!-- nav links -->

            {#each navLinks as link}
                <a
                    href={link.href}
                    class="text-xs uppercase text-white hover:text-opacity-80 transition-colors duration-300 ease-in-out"
                >
                    {link.name}
                </a>
            {/each}

            {#if signoutLoading}
                <span class="px-4 scale-75"> 
                    <Loader />
                </span>
            {:else}
                <button
                    on:click={handleSignOut}
                    class="text-xs uppercase text-white hover:text-opacity-80 transition-colors duration-300 ease-in-out"
                    class:hidden={!session}
                >
                    Sign out
                </button>
            {/if}

            <div id="google-translate-element"></div>
        </div>
    </div>
</nav>
