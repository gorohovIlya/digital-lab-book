<template>
  <div class="profile-page">
    <header class="header dev">
      <div class="to-main btn dev center-align">
        <router-link to="/" class="black-text not-a-link">На главную</router-link>
      </div>
      <div class="greeting dev center-align">Приветствие</div>
      <div class="edit btn dev center-align">
        <router-link to="/edit-profile" class="black-text not-a-link">Редактировать</router-link>
      </div>
      <div class="logout btn dev center-align">
        <router-link to="/authorize" class="white-text not-a-link">Выйти</router-link>
      </div>
    </header>
    <main class="main dev">
      <section class="personal-info-and-image dev">
        <div class="image-holder dev">Изображение</div>
        <div class="personal-info dev">
          <div class="item dev">E-mail</div>
          <div class="item dev">Фамилия</div>
          <div class="item dev">Имя</div>
          <div class="item dev">Отчество</div>
        </div>
      </section>
      <div class="experiments-and-departments dev">
        <div class="departments dev">Мои подразделения</div>
        <div class="control-panel dev">Панель управления (переключение страниц + добавить новое)</div>
        <div class="experiments dev">Мои эксперименты</div>
        <div class="control-panel dev">Панель управления (переключение страниц + добавить новое)</div>
      </div>
    </main>
  </div>
</template>

<script></script>

<style lang="scss" src="./ProfilePage.scss" scoped></style>
