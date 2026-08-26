<template>
  <div class="profile-page">
    <header class="header dev">
      <div class="to-main btn dev center-align">На главную</div>
      <div class="greeting dev center-align">Приветствие</div>
      <div class="edit btn dev center-align">Редактировать</div>
      <div class="logout btn dev center-align">Выйти</div>
    </header>
  </div>
</template>

<script>
</script>

<style>
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

</style>
