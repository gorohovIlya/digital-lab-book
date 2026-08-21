<template>
  <div class="register-page">
    <nav>
      <router-link to="/">На главную</router-link>
    </nav>
    <main>
      <div class="form-body">
        <form>
          <!--Поле ввода фамилии-->
          <p>
            <label for="lastname">Фамилия:</label>
            <input
              type="text"
              name="lastname"
              id="lastname"
              required
            >
          </p>
          <!--Поле ввода имени-->
          <p>
            <label for="name">Имя:</label>
            <input
              type="text"
              name="name"
              id="name"
              required
            >
          </p>
          <!--Поле ввода отчества-->
          <p>
            <label for="patronimyc">Отчество:</label>
            <input
              type="text"
              name="patronimyc"
              id="patronimyc"
              required
            >
          </p>
          <!--Поле выбора подразделения (пока хардкод)-->
          <p>
            <label for="department">Подразделение:</label>

              <select name="department" id="department" v-model="formData.department">
                <option value="1">Подразделение 1</option>
                <option value="2">Подразделение 2</option>
                <option value="3">Подразделение 3</option>
              </select>
          </p>
          <!--Поле выбора должности (пока хардкод)-->
          <p>
            <label for="post">Должность</label>
              <select name="post" id="post" v-model="formData.post">
                <option value="1">Должность 1</option>
                <option value="2">Должность 2</option>
                <option value="3">Должность 3</option>
              </select>
          </p>
          <p>
            <label for="email">E-mail:</label>
            <input
              type="email"
              name="email"
              id="email"
              required
            >
          </p>
          <p>
            <label for="password">Пароль:</label>
            <input
              type="password"
              name="password"
              id="password"
              required
            >
          </p>
          <p>
            <label for="password_repeat">Повторите пароль:</label>
            <input
              type="password"
              name="password_repeat"
              id="password_repeat"
              required
            >
          </p>
          <button type="submit">Зарегистрироваться</button>
        </form>
      </div>
    </main>
  </div>
</template>
