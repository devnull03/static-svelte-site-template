<script lang="ts">
  const navLinks = [
    {
      name: "Home",
      href: "/",
    },
    // {
    //   name: "My test",
    //   href: "/about",
    // },
    // {
    //   name: "Logout",
    //   href: "/contact",
    // },
    
  ];

</script>

<nav class="">
  <div
    class="top-0 bg-sky-500 h-16 w-full flex flex-row justify-between items-center fixed z-50 "
  >
    <!-- top fixed -->
    <div class="flex text-white font-bold items-center ps-4 "> the driving school</div>

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
    </div>

    
  </div>
</nav>
