<script lang="ts">
    import { page } from "$app/stores";

    $: testType = $page.params 

    $: console.log(testType);
    

</script>


