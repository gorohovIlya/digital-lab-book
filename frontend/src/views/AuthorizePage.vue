<template>
  <div class="authorize-page">
    <nav>
      <router-link to="/">На главную</router-link>
    </nav>

    <main>
      <div class="form-body">
        <form @submit.prevent="handleSubmit">
          <p>
            <label for="email">E-mail:</label>
            <input
              type="email"
              name="email"
              id="email"
              v-model="formData.email"
              required
            >
          </p>
          <p>
            <label for="password">Пароль:</label>
            <input
              type="password"
              name="password"
              id="password"
              v-model="formData.password"
              required
            >
          </p>
          <button type="submit">Войти</button>
        </form>
      </div>
      <router-link to="/register">Регистрация</router-link>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        email: '',
        password: ''
      },
      loading: false,
      error: null,
    };
  },
  methods: {
    async handleSubmit() {
      console.log('Запрос данных...', this.formData);
      try {
        const response = await axios.post('http://localhost:8000/api/login', this.formData);
        console.log('Success: ', response.data);
        // const { access_token, user_id, user_name, user_lastname, user_patronymic, user_email} = response.data;
      } catch (error) {
        console.error('Error: ', error);
      }
    }
  }
}
</script>
