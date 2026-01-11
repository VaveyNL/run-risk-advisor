def calculate_risk(run_plan, weather, air, profile):
    risk = 0

    intensity_risk = {
        "low": 20,
        "medium": 40,
        "high": 60,
    }
    risk += intensity_risk.get(run_plan.intensity, 30)

    risk += min(run_plan.duration_min / 60 * 20, 20)

    if weather["temp"] < 0 or weather["temp"] > 30:
        risk += 15

    if weather["condition"] in ["rain", "snow", "storm"]:
        risk += 20

    if weather["wind"] > 7:
        risk += 10

    if air["pm25"] > profile.pm25_limit:
        risk += 25

    sensitivity_bonus = {
        "low": 0,
        "medium": 10,
        "high": 20,
    }
    risk += sensitivity_bonus.get(profile.sensitivity_level, 10)

    risk = min(int(risk), 100)

    if risk < 35:
        return risk, "low", "Условия благоприятны для пробежки."
    elif risk < 70:
        return risk, "medium", "Рекомендуется умеренный темп и контроль самочувствия."
    else:
        return risk, "high", "Высокий риск. Рассмотрите перенос тренировки."
