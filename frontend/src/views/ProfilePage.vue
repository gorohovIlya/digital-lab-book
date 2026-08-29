<template>
  <div class="profile-page">
    <header class="header dev">
      <div class="to-main btn dev center-align">На главную</div>
      <div class="greeting dev center-align">Приветствие</div>
      <div class="edit btn dev center-align">Редактировать</div>
      <div class="logout btn dev center-align">Выйти</div>
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

<style lang="scss" scoped>
@use "sass:color";

// --- ПЕРЕМЕННЫЕ ---
$main-color: #ccc;
$to-main-btn-color: #70a4d4;
$edit-btn-color:  #84d1d1;
$logout-btn-color: darkred;
$header-element-height: 60%;
$base-width: 96%;
$lighten-amount: 15%;
$header-font-size: 22px;
$base-border-radius: 12px;

// --- УНИВЕРСАЛЬНЫЙ МИКСИН ---
@mixin flex($direction: row, $justify: center, $align: center) {
  display: flex;
  flex-direction: $direction;
  justify-content: $justify;
  align-items: $align;
}

// --- СТИЛИ СТРАНИЦЫ ---
.profile-page {
  @include flex(column, space-between, stretch);
  height: 100%;
  background-color: $main-color;

  // Служебный класс для разработки
  .dev {
    border: 2px solid grey;
  }

  // Общий вспомогательный класс
  .center-align {
    @include flex;
  }

  // Шапка сайта
  .header {
    @include flex(row, space-around, center);
    position: fixed;
    top: 0;
    left: 2%;
    width: $base-width;
    height: 80px;
    padding: 0.5%;
    margin-bottom: 10px;
    border-radius: $base-border-radius;
    background-color: azure;
    z-index: 10;
  }

  .greeting {
    width: 50%;
    height: $header-element-height;
    margin-top: 0.5%;
    font-weight: bold;
    font-size: $header-font-size;
  }

  // Блок кнопок (все кнопки в одном месте)
  .btn {
    height: $header-element-height;
    margin-top: 0.5%;
    border-radius: 10px;
    font-weight: bold;
    font-size: $header-font-size;
    transition: background-color 0.2s ease, transform 0.1s ease; // Плавность анимации

    &:hover {
      cursor: pointer;
    }

    &:active {
      transform: scale(0.95);
    }

    // Модификаторы кнопок
    &.to-main {
      background-color: $to-main-btn-color;
      width: 13%;
      &:hover {
        background-color: color.adjust($to-main-btn-color, $lightness: $lighten-amount);
      }
    }

    &.edit {
      background-color: $edit-btn-color;
      width: 15%;
      &:hover {
        background-color: color.adjust($edit-btn-color, $lightness: $lighten-amount);
      }
    }

    &.logout {
      background-color: $logout-btn-color;
      color: white;
      width: 10%;
      &:hover {
        background-color: color.adjust($logout-btn-color, $lightness: $lighten-amount);
      }
    }
  }

  // Главный контент
  .main {
    @include flex(row, space-between, stretch);
    width: $base-width;
    height: 840px;
    margin-left: 2%;
    margin-top: 90px; // Отступ сверху, чтобы контент не залезал под fixed-шапку
    padding: 0.5%;
    border-radius: $base-border-radius;
    background-color: azure;
  }

  // Левая колонка (Инфо и Аватар)
  .personal-info-and-image {
    @include flex(column, space-between, stretch);
    width: 33%;
    height: 98.5%;
    border-radius: 12px;

    .image-holder {
      height: 60%;
      margin: 0 5%;
    }

    .personal-info {
      @include flex(column, space-between, stretch);
      height: 38%;
      margin: 0 5%;

      .item {
        height: 20%;
      }
    }
  }

  // Правая колонка (Списки и управление)
  .experiments-and-departments {
    @include flex(column, space-between, stretch);
    width: 66.5%;
    border-radius: $base-border-radius;

    .departments {
      height: 33%;
    }

    .experiments {
      height: 53%;
    }

    .control-panel {
      width: 35%;
      height: 6%;
      margin-left: 65%;
    }
  }
}
</style>
