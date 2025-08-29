import quackApi from "../api/quackApi";

export const getSchedule = async (payload) => {
  const { data } = await quackApi.post(
    "/api/schedule/",
    payload,
    {
      headers: {
        "Content-Type": "application/json",
      }
    }
  );
  return data;
};
