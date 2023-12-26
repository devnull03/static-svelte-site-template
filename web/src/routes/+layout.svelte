<script>
    import Footer from "$lib/Footer.svelte";
    import Header from "$lib/Header.svelte";
    import "../app.css";
</script>

<svelte:head>
    <title>{import.meta.env.VITE_COMPANY_NAME}</title>
</svelte:head>

<Header />
<div class="h-screen flex flex-col justify-between pt-20">
    <slot />
    <div>
        <!-- <Footer /> -->
    </div>
</div>
