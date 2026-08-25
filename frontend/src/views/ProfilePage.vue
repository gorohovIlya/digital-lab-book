<template>
  <div class="profile-page dev">
    <header class="header dev">
      <div class="greeting dev"></div>
      <div class="edit btn dev"></div>
      <div class="logout btn dev"></div>
    </header>
  </div>
</template>

<script>
</script>

<style>
.dev {
    border: 2px solid blue;
}

.profile-page {
  width: 100%;
  height: 100%;
}

.header {
  border-radius: 12px;
  position: fixed;
  display: flex;
  flex-direction: row;
  margin: 5% 10%;
  padding: 3%;
  width: 80%;
  height: 16%;
}
.greeting {
  width: 70%;
  height: 80%;
}

</style>
