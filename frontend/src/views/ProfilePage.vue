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

<style>
.profile-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  background-color: #ccc;
}
.dev {
  border: 2px solid grey;
}

.center-align {
  display: flex;
  align-items: center;
  justify-content: center;
}

.header {
  border-radius: 12px;
  position: fixed;
  display: flex;
  flex-direction: row;
  margin-left: 2%;
  width: 96%;
  padding: 0.5%;
  height: 80px;
  justify-content: space-around;
  background-color: azure;
  margin-bottom: 10px;
}
.greeting {
  width: 50%;
  height: 60%;
  margin-top: 0.5%;
  font-weight: bold;
  font-size: 22px;
}
.btn {
  height: 60%;
  margin-top: 0.5%;
  border-radius: 10px;
  font-weight: bold;
  font-size: 22px;
}

.to-main {
  background-color: #70a4d4;
  width: 13%;
}

.edit {
  background-color: #84d1d1;
  width: 15%;
}

.logout {
  background-color: darkred;
  color: white;
  width: 10%;
}

.btn:hover {
  cursor: pointer;
}

.to-main:hover {
  background-color: #aecae6;
}

.edit:hover {
  background-color: #aee6e6;
}

.btn:active {
  transform: scale(0.98);
}

.logout:hover {
  background-color: #ba2929;
}

.main {
  margin-left: 2%;
  width: 96%;
  padding: 0.5%;
  height: 500px;
  margin-top: 5%;
  border-radius: 12px;
  height: 840px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: azure;
}

.personal-info-and-image {
  width: 33%;
  height: 98.5%;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
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
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.item {
  height: 20%;
}

.experiments-and-departments {
  width: 66.5%;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
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
