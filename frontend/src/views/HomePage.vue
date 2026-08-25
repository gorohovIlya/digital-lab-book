<template>
  <div class="home-page">
    <header class="links-container">
      <router-link to="/edit">Редактирование</router-link>
      <router-link to="/authorize">Войти</router-link>
      <router-link to="/profile">Макет профиля</router-link>
    </header>
  </div>
</template>

<style>
  .home-page {
    width: 100%;
    height: 100%;
  }
  .links-container {
    width: 20%;
    height: 25%;
    display: flex;
    flex-direction: column;
  }
</style>
