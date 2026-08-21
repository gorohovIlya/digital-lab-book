<template>
  <div class="edit-page">
    <!-- Навигация -->
    <nav>
      <div class="department-name">
        Наименование подразделения
      </div>
    </nav>

    <!-- Основной контент -->
    <main>
      <!-- Информационная таблица -->
      <div class="info-table">
        <div class="info-table-item">
          <div class="label-div">
            <label for="datetime">Дата:</label>
          </div>
          <div class="text-div">
            <input type="text" id="datetime" name="datetime">
          </div>
        </div>

        <div class="info-table-item">
          <div class="label-div">
            <label for="project-name">Наименование проекта:</label>
          </div>
          <div class="text-div">
            <input type="text" id="project-name" name="project-name">
          </div>
        </div>

        <div class="info-table-item">
          <div class="label-div">
            <label for="exp-num">Номер эксперимента:</label>
          </div>
          <div class="text-div">
            <input type="text" id="exp-num" name="exp-num">
          </div>
        </div>

        <div class="info-table-item">
          <div class="label-div">
            <label for="exp-comment">Комментарий:</label>
          </div>
          <div class="text-div">
            <textarea id="exp-comment" name="exp-comment" rows="7" cols="4"></textarea>
          </div>
        </div>

        <div class="info-table-item">
          <div class="label-div">
            <label for="exp-goal">Цель эксперимента:</label>
          </div>
          <div class="text-div">
            <textarea id="exp-goal" name="exp-goal" rows="7" cols="4"></textarea>
          </div>
        </div>
      </div>

      <!-- Таблица веществ -->
      <div class="substances-table">
        <div class="substances-table-header">
          <div class="cell">Вещество</div>
          <div class="cell">CAS-Номер</div>
          <div class="cell">Кол-во Вещества</div>
          <div class="cell">Молярная масса</div>
          <div class="cell">Масса</div>
          <div class="cell">Плотность</div>
          <div class="cell">Объем</div>
        </div>
      </div>

      <!-- Методика -->
      <div class="methodic">
        <div class="methodic-header">
          Методика *назв. вещества*
        </div>
        <div class="methodic-chemdraw-embedded">
          chemdraw встройка
        </div>
        <div class="methodic-substances-table">
          В-во 1
        </div>
      </div>

      <!-- Таблица продуктов -->
      <div class="products-table">
        <div class="products-table-header">
          <div class="products-table-header-item">Продукты</div>
          <div class="products-table-header-item">Масса</div>
          <div class="products-table-header-item">Объем</div>
        </div>
      </div>

      <!-- Панель управления -->
      <div class="control-panel">
        <div class="button save">Сохранить</div>
        <div class="button exit">Выйти</div>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Все стили из style.css */
.department-name {
  width: 98.5%;
  text-align: right;
  padding: 0.5%;
}

.info-table {
  width: 98.5%;
  display: grid;
  padding: 0.5%;
  margin-bottom: 1%;
  margin-top: 1%;
}

.info-table-item {
  width: 98.5%;
  padding: 0.5%;
  display: flex;
  flex-direction: row;
}

.label-div {
  width: 12%;
  padding: 0.5%;
}

.text-div {
  width: 86%;
  padding: 0.5%;
  font-size: 20px;
}

input {
  width: 20%;
}

textarea {
  width: 33%;
}

.substances-table {
  width: 98.5%;
  padding: 0.5%;
  margin-bottom: 1%;
}

.substances-table-header {
  display: grid;
  grid-auto-flow: column;
}

.methodic {
  padding: 0.5%;
  width: 98.5%;
  display: grid;
  margin-bottom: 1%;
}

.methodic-substances-table {
  display: grid;
}

.products-table {
  display: grid;
  padding: 0.5%;
  margin-bottom: 1%;
}

.products-table-header {
  display: grid;
  grid-auto-flow: column;
}

.control-panel {
  display: grid;
  grid-auto-flow: column;
  gap: 20%;
  padding-left: 10%;
  padding-right: 10%;
  padding-top: 0.5%;
  padding-bottom: 0.5%;
}

 .dev {
  border: 2px solid blue;
}

/* Кнопки */
.button {
  padding: 10px 20px;
  text-align: center;
  cursor: pointer;
  border-radius: 5px;
  font-weight: bold;
}

.save {
  background-color: #4CAF50;
  color: white;
}

.exit {
  background-color: #f44336;
  color: white;
}

.button:hover {
  opacity: 0.8;
}
</style>
