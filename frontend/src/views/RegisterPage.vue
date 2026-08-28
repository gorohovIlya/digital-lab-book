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
          <div class="departments-field dev">
            <div class="label-div dev">
              <label>Подразделение:</label>
            </div>
            <div class="all-departments dev">
              <div class="department dev" v-for="(department_name, department_id) in departments" :key="department_id">
                <input
                  type="checkbox"
                  :id="department_id"
                  :value="department_id"
                  v-model="formData.departments"
                >
                <label :for="department_id">{{ department_name }}</label>
              </div>
            </div>
          </div>
          <!--Поле выбора должности (пока хардкод)-->
          <p>
            <label for="post">Должность</label>
              <select name="post" id="post" v-model="formData.post">
                <option value="1">Должность 1</option>
                <option value="2">Должность 2</option>
                <option value="3">Должность 3</option>
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
              :class="{ 'input-error': !passwordsMatch && formData.passwordRepeat }"
              required
            >
            <span v-if="!passwordsMatch && formData.passwordRepeat" class="error-text">
                Пароли не совпадают
            </span>
          </p>
          <button type="submit" :disabled="!isFormValid">Зарегистрироваться</button>
        </form>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      departments: {
        0: "Лаборатория непредельных гетероатомных соединений",
        1: "Лаборатория галогенорганических соединений",
        2: "Лаборатория элементоорганических соединений",
        3: "Лаборатория халькогенорганических соединений",
        4: "Лаборатория функциональных полимеров",
        5: "Лаборатория функциональных наноматериалов",
        6: "Лаборатория ядерного магнитного резонанса",
        7: "Лаборатория фотоактивных соединений",
        8: "Лаборатория структурных исследований",
        9: "Лаборатория экологической биотехнологии",
        10: "Лаборатория плазмохимических технологий в винилировании",
        11: "Лаборатория устойчивого развития Байкальского региона",
        12: "Лаборатории правовых исследований высокотехнологических отраслей производства",
        13: "Лаборатория лингво-педагогических исследований",
        14: "Центр инженерных разработок",
        15: "Байкальский аналитический центр коллективного пользования"
      },
      formData: {
        lastname: '',
        name: '',
        patronymic: '',
        departments: [],
        post: '',
        email: '',
        password: '',
        passwordRepeat: ''
      }
    }
  },
  computed: {
    passwordsMatch() {
      return this.formData.password === this.formData.passwordRepeat;
    },
    isFormValid() {
      return this.formData.password.length > 0 && this.passwordsMatch;
    },
    formDataToSend() {
      return {
        ...this.formData,
        departments: this.formData.departments.map(Number)
      };
    }
  },
  methods: {
    async handleSubmit() {
      console.log('Отправка данных на сервер...');
      console.log(JSON.stringify(this.formData, null, 2));
      try {
        const response = await axios.post('http://localhost:8000/api/submit', this.formDataToSend);
        console.log('Success: ', response.data);
      } catch (error) {
        console.error('Error: ', error)
      }
    }
  }
}
</script>


<style>
.input-error { border: 1px solid red; }
.error-text { color: red; font-size: 12px; display: block; }
.label-div {
  width: 34%;
  text-align: center;
}
.departments-field {
  display: flex;
  flex-direction: row;
  padding: 3px;
  margin-right: 3px;
  width: 34%;
}

.all-departments {
  display: flex;
  width: 66%;
  flex-direction: column;
  height: auto;
  margin-left: 3px;
  padding: 3px;
}

.department {
  display: flex;
  align-items: center;
  gap: 8px; /* отступ между чекбоксом и текстом */
  margin: 2px 0;
}

.department input[type="checkbox"] {
  margin: 0;
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.department label {
  cursor: pointer;
  font-size: 14px;
}

.dev {
  border: 2px solid blue;
  padding: 10px;
  margin: 5px 0;
}
</style>