<template>
  <div class="register-page">
    <nav>
      <router-link to="/">На главную</router-link>
    </nav>
    <main>
      <div class="form-body">
        <form @submit.prevent="handleSubmit">
          <!--Поле ввода фамилии-->
          <p>
            <label for="lastname">Фамилия:</label>
            <input
              type="text"
              v-model="formData.lastname"
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
              v-model="formData.name"
              name="name"
              id="name"
              required
            >
          </p>
          <!--Поле ввода отчества-->
          <p>
            <label for="patronymic">Отчество:</label>
            <input
              type="text"
              v-model="formData.patronymic"
              name="patronymic"
              id="patronymic"
              required
            >
          </p>
          <!--Поле выбора подразделения (пока хардкод)-->
          <p>
            <label for="department">Подразделение:</label>
              <select name="department" id="department" v-model="formData.department">
                <option value="Подразделение_1">Подразделение 1</option>
                <option value="Подразделение_2">Подразделение 2</option>
                <option value="Подразделение_3">Подразделение 3</option>
              </select>
          </p>
          <!--Поле выбора должности (пока хардкод)-->
          <p>
            <label for="post">Должность</label>
              <select name="post" id="post" v-model="formData.post">
                <option value="Должность_1">Должность 1</option>
                <option value="Должность_2">Должность 2</option>
                <option value="Должность_3">Должность 3</option>
              </select>
          </p>
          <!--Поле ввода E-mail:-->
          <p>
            <label for="email">E-mail:</label>
            <input
              type="email"
              v-model="formData.email"
              name="email"
              id="email"
              required
            >
          </p>
          <!--Поле ввода пароля:-->
          <p>
            <label for="password">Пароль:</label>
            <input
              type="password"
              v-model="formData.password"
              name="password"
              id="password"
              required
            >
          </p>
          <!--Поле повторного ввода пароля-->
          <p>
            <label for="password_repeat">Повторите пароль:</label>
            <input
              type="password"
              v-model="formData.passwordRepeat"
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

<script>
export default {
  data() {
    return {
      formData: {
        lastname: '',
        name: '',
        patronymic: '',
        department: '',
        post: '',
        email: '',
        password: '',
        passwordRepeat: ''
      }
    }
  },
}
</script>
