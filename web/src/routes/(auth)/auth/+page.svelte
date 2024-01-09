<!-- // src/routes/auth/+page.svelte -->
<script lang="ts">
    export let data;
    let { supabase } = data;
    $: ({ supabase } = data);

    let email: string;
    let password: string;

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

<div class="mt-20 flex flex-col gap-8 items-center">
    <form
        on:submit={signInWithEmail}
        class="bg-gray-100 flex flex-col gap-4 w-1/2 items-center"
    >
        <h1 class="text-2xl">Sign In</h1>

        <span>
            Email:
            <input id="email" name="email" bind:value={email} />
        </span>

        <button>Sign in</button>

    </form>

</div>
