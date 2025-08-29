import axios from "axios";

const quackApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

quackApi.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export default quackApi;
