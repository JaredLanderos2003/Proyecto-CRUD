import React, { useState } from 'react';
import Menu from './Menu'; // Asegúrate de importar el componente del menú
import './Grades.css';

const GradesCapture = () => {
  const [enrollments, setEnrollments] = useState([
    { student: 'Jared Noe Landeros', subject: 'Desarrollo Colaborativo' },
  ]); 
  const [grades, setGrades] = useState([]);
  const [selectedEnrollment, setSelectedEnrollment] = useState('');
  const [grade, setGrade] = useState('');
  const [error, setError] = useState('');

  const handleAddGrade = () => {
    if (!selectedEnrollment || grade === '') {
      setError('Por favor selecciona una inscripción y captura una calificación.');
      return;
    }
    if (isNaN(grade) || grade < 0 || grade > 100) {
      setError('La calificación debe ser un número entre 0 y 100.');
      return;
    }
    const [student, subject] = selectedEnrollment.split(' → ');
    const existingGrade = grades.find(
      (g) => g.student === student && g.subject === subject
    );
    if (existingGrade) {
      setError('Ya se capturó una calificación para esta inscripción.');
      return;
    }
    setGrades([...grades, { student, subject, grade }]);
    setSelectedEnrollment('');
    setGrade('');
    setError('');
  };

  const handleDeleteGrade = (index) => {
    const updatedGrades = grades.filter((_, i) => i !== index);
    setGrades(updatedGrades);
  };

  return (
    <div className="grades-capture-container">
      <img src="/i1.png" alt="EduManage Logo" className="login-logo" />
      <Menu /> {/* Agrega el menú aquí */}
      <h1>Captura de Calificaciones</h1>
      <div className="form">
        <select
          value={selectedEnrollment}
          onChange={(e) => setSelectedEnrollment(e.target.value)}
        >
          <option value="">Selecciona Inscripción</option>
          {enrollments.map((enrollment, index) => (
            <option
              key={index}
              value={`${enrollment.student} → ${enrollment.subject}`}
            >
              {enrollment.student} → {enrollment.subject}
            </option>
          ))}
        </select>
        <input
          type="number"
          placeholder="Calificación"
          value={grade}
          onChange={(e) => setGrade(e.target.value)}
        />
        <button onClick={handleAddGrade}>Capturar</button>
        {error && <p className="error">{error}</p>}
      </div>
      <div className="grades-list-container">
        <ul className="grades-list">
          {grades.map((gradeItem, index) => (
            <li key={index}>
              {gradeItem.student} → {gradeItem.subject}: {gradeItem.grade}
              <button onClick={() => handleDeleteGrade(index)}>Eliminar</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default GradesCapture;
