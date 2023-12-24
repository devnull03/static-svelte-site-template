<script>
    import Footer from "$lib/Footer.svelte";
    import Header from "$lib/Header.svelte";
    import Table from "$lib/table.svelte";
    import "../app.css";
</script>

<svelte:head>
    <title>{import.meta.env.VITE_COMPANY_NAME}</title>
</svelte:head>

<div class="h-screen flex flex-col justify-between">
    <Header />
    <main class="h-full mt-16">
      <div class="flex items-center justify-center pt-8 md:flex-row lg:flex-row sm:flex-col"> 
        <Table heading="Learn Test"/>
        <Table heading="Practise Test"/>
      </div>
        
    </main>
    <Footer />
</div>
<slot />

