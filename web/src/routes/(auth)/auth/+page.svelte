<!-- // src/routes/auth/+page.svelte -->
<script lang="ts">
    import { fly, slide } from 'svelte/transition';

    export let data;
    let { supabase } = data;
    $: ({ supabase } = data);

    let email: string;
    let password: string;

    let showMessage = false;

    const handleSignUp = async (event: SubmitEvent) => {
        event.preventDefault();
        let res = await supabase.auth.signUp({
            email,
            password,
            options: {
                emailRedirectTo: `${location.origin}/auth/callback`,
            },
        });
        console.log(res);
    };

    const handleSignIn = async () => {
        let res = await supabase.auth.signInWithPassword({
            email,
            password,
        });

        console.log(res);
    };

    const handleSignOut = async () => {
        let res = await supabase.auth.signOut();
        console.log(res);
    };

    async function signInWithEmail(event: SubmitEvent) {
        event.preventDefault();

        showMessage = true;

        return;

        let res = await supabase.auth.signInWithOtp({
            email,
            options: {
                // set this to false if you do not want the user to be automatically signed up
                shouldCreateUser: false,
                emailRedirectTo: `${location.origin}/auth/callback`,
            },
        });

        console.log(res);
    }
</script>

<div class="mt-20 flex flex-col gap-8 items-center px-4">
    <form
        on:submit={signInWithEmail}
        class="bg-gray-100 flex flex-col gap-6 w-full lg:w-1/2 h-[50vh] items-center justify-center rounded-lg relative"
    >
        <div class="top-8 absolute text-center">
            <h1 class="text-4xl font-bold pb-4">Sign In</h1>
            <p class="text-sm">Enter your email and click the link in your inbox to sign in.</p>
        </div>

        <span class="flex flex-row gap-4 items-center pt-8">
            <span class="text-lg"> Email: </span>
            <input
                class="outline-none rounded-md px-2 py-1 shadow"
                placeholder="example@domain.com"
                id="email"
                type="email"
                name="email"
                bind:value={email}
            />
        </span>

        {#if showMessage}
            <div transition:slide={{  }}>
                <p class="text-sm">Check your email for the magic link!</p>
            </div>
        {/if}

        <button
            class="border py-1 px-2 rounded-md shadow font-light hover:scale-105 active:scale-100 ease-linear duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            disabled={!email || showMessage}
            >Sign in</button
        >
    </form>
</div>
