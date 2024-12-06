import React, { useState } from 'react';
import { useStudents } from '../context/StudentsContext'; // Importa el contexto de estudiantes
import { useSubjects } from '../context/SubjectsContext'; // Importa el contexto de materias
import './Enrollment.css';

const Enrollment = () => {
  const { students } = useStudents(); // Obtén los estudiantes
  const { subjects } = useSubjects(); // Obtén las materias
  const [selectedStudent, setSelectedStudent] = useState('');
  const [selectedSubject, setSelectedSubject] = useState('');
  const [enrollments, setEnrollments] = useState([]);

  const handleEnrollment = () => {
    if (selectedStudent && selectedSubject) {
      setEnrollments([...enrollments, { student: selectedStudent, subject: selectedSubject }]);
      setSelectedStudent('');
      setSelectedSubject('');
    }
  };

  return (
    <div className="enrollment-container">
      <h1>Inscripción de Estudiantes</h1>
      <select value={selectedStudent} onChange={(e) => setSelectedStudent(e.target.value)}>
        <option value="">Selecciona un Estudiante</option>
        {students.map((student, index) => (
          <option key={index} value={`${student.name} ${student.lastName}`}>
            {student.name} {student.lastName} ({student.career})
          </option>
        ))}
      </select>
      <select value={selectedSubject} onChange={(e) => setSelectedSubject(e.target.value)}>
        <option value="">Selecciona una Materia</option>
        {subjects.map((subject, index) => (
          <option key={index} value={subject.name}>
            {subject.name} - {subject.teacher} ({subject.schedule})
          </option>
        ))}
      </select>
      <button onClick={handleEnrollment}>Inscribir</button>

      <div className="enrollment-list">
        <h2>Estudiantes Inscritos</h2>
        <ul>
          {enrollments.map((enrollment, index) => (
            <li key={index}>
              {enrollment.student} inscrito en {enrollment.subject}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Enrollment;
