<!-- // src/routes/auth/+page.svelte -->
<script lang="ts">
    import { goto } from "$app/navigation";
    import { fly, slide } from "svelte/transition";

    export let data;
    let { supabase, session } = data;
    $: ({ supabase, session } = data);

    let email: string;
    let otp: string;
    let errorMessage: string = "";

    let otpSent = false;

    const handleSignIn = async () => {
        console.log(email, otp);

        let res = await supabase.auth.verifyOtp({
            email,
            token: otp,
            type: "email",
        });

        console.log(res);

        if (res.error) {
            errorMessage = res.error.message;
        } else {
            // console.log(res);
            // session = res;
            goto("/");
        }
    };

    const handleSignOut = async () => {
        let res = await supabase.auth.signOut();
        console.log(res);
    };

    async function signInWithEmail() {
        let res = await supabase.auth.signInWithOtp({
            email,
            options: {
                // set this to false if you do not want the user to be automatically signed up
                shouldCreateUser: false,
                emailRedirectTo: `${location.origin}/auth/callback`,
            },
        });

        console.log(res);

        if (res.error) {
            errorMessage = res.error.message;
        } else {
            otpSent = true;
        }
    }
</script>

<div class="mt-20 flex flex-col gap-8 items-center px-4">
    <div
        class="bg-gray-100 flex flex-col gap-2 w-full lg:w-1/2 h-[50vh] items-center justify-center rounded-lg relative"
    >
        <div class="top-8 absolute text-center">
            <h1 class="text-4xl font-bold pb-4">Sign In</h1>
            <p class="text-sm">
                Enter your email and click the link in your inbox to sign in.
            </p>
        </div>

        <span class="flex flex-row gap-4 items-center pt-8">
            <span class="text-lg"> Email: </span>
            <input
                class="outline-none rounded-md px-2 py-1 shadow"
                placeholder="example@domain.com"
                disabled={otpSent}
                id="email"
                type="email"
                name="email"
                bind:value={email}
            />
        </span>

        {#if otpSent}
            <span transition:slide class="flex flex-row gap-4 items-center">
                <span class="text-lg"> OTP: </span>
                <input
                    class="outline-none rounded-md px-2 py-1 shadow"
                    placeholder="123456"
                    id="otp"
                    type="text"
                    name="otp"
                    bind:value={otp}
                />
            </span>
        {/if}

        {#if errorMessage}
            <div transition:slide>
                <p class="text-sm text-red-500">{errorMessage}</p>
            </div>
        {/if}

        <button
            on:click={(e) => {
                e.preventDefault();

                if (otpSent) {
                    handleSignIn();
                } else {
                    signInWithEmail();
                }
            }}
            class="border py-1 px-2 rounded-md shadow font-light hover:scale-105 active:scale-100 ease-linear duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            disabled={!email || (otpSent && !otp)}
        >
            {#if otpSent}
                Sign In
            {:else}
                Send OTP
            {/if}
        </button>
    </div>
</div>
