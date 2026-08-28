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

<style lang="scss">
@use "sass:color";
$main-color: #ccc;
$to-main-btn-color: #70a4d4;
$edit-btn-color:  #84d1d1;
$logout-btn-color: darkred;
$header-element-height: 60%;
$base-width: 96%;
$lighten-amount: 15%;
$header-font-size: 22px;
$base-border-radius: 12px;

@mixin flex-vertical-sp-between ($direction: column, $justify: space-between) {
  display: flex;
  flex-direction: $direction;
  justify-content: $justify;
}

@mixin flex-center-align ($align: center, $justify: center) {
  display: flex;
  align-items: $align;
  justify-content: $justify;
}

@mixin flex-horizontal-sp-around ($direction: row, $justify: space-around) {
  display: flex;
  flex-direction: $direction;
  justify-content: $justify;
}

.profile-page {
  @include flex-vertical-sp-between;
  height: 100%;
  background-color: $main-color;
}
.dev {
  border: 2px solid grey;
}

.center-align {
  @include flex-center-align;
}

.header {
  border-radius: $base-border-radius;
  position: fixed;
  margin-left: 2%;
  width: $base-width;
  padding: 0.5%;
  height: 80px;
  background-color: azure;
  margin-bottom: 10px;
  @include flex-horizontal-sp-around;
}
.greeting {
  width: 50%;
  height: $header-element-height;
  margin-top: 0.5%;
  font-weight: bold;
  font-size: $header-font-size;
}
.btn {
  height: $header-element-height;
  margin-top: 0.5%;
  border-radius: 10px;
  font-weight: bold;
  font-size: $header-font-size;

  &:hover {
    cursor: pointer;
  }

  &:active {
    transform: scale(0.95);
  }
}

.to-main {
  background-color: $to-main-btn-color;
  width: 13%;
  &:hover {
    background-color: color.adjust($to-main-btn-color, $lightness: $lighten-amount);
  }
}

.edit {
  background-color: $edit-btn-color;
  width: 15%;
  &:hover {
    background-color: color.adjust($edit-btn-color, $lightness: $lighten-amount);
  }
}

.logout {
  background-color: $logout-btn-color;
  color: white;
  width: 10%;
  &:hover {
    background-color: color.adjust($logout-btn-color, $lightness: $lighten-amount);
  }
}

.main {
  margin-left: 2%;
  width: $base-width;
  padding: 0.5%;
  margin-top: 5%;
  border-radius: $base-border-radius;
  height: 840px;
  @include flex-horizontal-sp-around($justify: space-between);
  background-color: azure;
}

.personal-info-and-image {
  width: 33%;
  height: 98.5%;
  border-radius: 12px;
  @include flex-vertical-sp-between;
}

.image-holder {
  height: 60%;
  margin-left: 5%;
  margin-right: 5%;
}

.personal-info {
  height: 38%;
  margin-left: 5%;
  margin-right: 5%;
  @include flex-vertical-sp-between;
}

.item {
  height: 20%;
}

.experiments-and-departments {
  width: 66.5%;
  border-radius: $base-border-radius;
  @include flex-vertical-sp-between;
}

.departments {
  height: 33%;
}

.experiments {
  height: 53%;
}

.control-panel {
  height: 6%;
  width: 35%;
  margin-left: 65%;
}

</style>
