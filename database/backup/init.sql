CREATE SCHEMA IF NOT EXISTS sl_schema;

CREATE TABLE sl_schema.sl_data (
    stress_level_description TEXT,
    mental_health_history_description TEXT,
    living_conditions_description TEXT,
    academic_performance_description TEXT,
    anxiety_level INT,
    self_esteem INT,
    mental_health_history INT,
    depression INT,
    headache INT,
    blood_pressure INT,
    sleep_quality INT,
    breathing_problem INT,
    noise_level INT,
    living_conditions INT,
    safety INT,
    basic_needs INT,
    academic_performance INT,
    study_load INT,
    teacher_student_relationship INT,
    future_career_concerns INT,
    social_support INT,
    peer_pressure INT,
    extracurricular_activities INT,
    bullying INT,
    stress_level INT
);

COPY sl_schema.sl_data
FROM '/dataset/StressLevelDataset.csv'
DELIMITER ','
CSV HEADER;
