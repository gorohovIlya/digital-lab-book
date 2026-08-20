<template>
  <div class="authorize-page">
    <nav>
      <router-link to="/">На главную</router-link>
    </nav>

    <main>
      <div class="form-body">
        <form>
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
          <button type="submit">Войти</button>
        </form>
      </div>
      <router-link to="/register">Регистрация</router-link>
    </main>
  </div>
</template>
