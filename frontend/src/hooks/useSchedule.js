import { useState } from "react";
import { getSchedule } from "../services/scheduleService";

export const useSchedule = () => {
  const [scheduleData, setScheduleData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchSchedule = async (payload) => {
    setLoading(true);
    setError(null);

    try {
      const data = await getSchedule(payload);
      setScheduleData(data);
      return data;
    } catch (err) {
      setError(err);
      throw err; 
    } finally {
      setLoading(false);
    }
  };

  return { scheduleData, loading, error, fetchSchedule };
};
