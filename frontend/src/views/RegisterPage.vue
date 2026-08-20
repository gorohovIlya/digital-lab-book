<template>
  <div class="register-page">
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
