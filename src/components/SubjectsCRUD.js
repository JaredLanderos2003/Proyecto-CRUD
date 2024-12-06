import React, { useState } from 'react';
import { useSubjects } from '../context/SubjectsContext';
import Menu from './Menu';
import './SubjectsCRUD.css';

const SubjectsCRUD = () => {
  const { subjects, setSubjects } = useSubjects();
  const [newSubject, setNewSubject] = useState('');
  const [teacher, setTeacher] = useState('');
  const [schedule, setSchedule] = useState('');
  const [editIndex, setEditIndex] = useState(null);
  const [error, setError] = useState('');

  const handleAddSubject = () => {
    if (newSubject.trim() === '' || teacher.trim() === '' || schedule.trim() === '') {
      setError('Todos los campos deben ser llenados.');
      return;
    }

    const newSubjects = [...subjects, { name: newSubject, teacher, schedule }];
    setSubjects(newSubjects);
    setNewSubject('');
    setTeacher('');
    setSchedule('');
    setError('');
  };

  const handleEditSubject = (index) => {
    const subject = subjects[index];
    setNewSubject(subject.name);
    setTeacher(subject.teacher);
    setSchedule(subject.schedule);
    setEditIndex(index);
  };

  const handleSaveEdit = () => {
    if (newSubject.trim() === '' || teacher.trim() === '' || schedule.trim() === '') {
      setError('Todos los campos deben ser llenados.');
      return;
    }

    const updatedSubjects = [...subjects];
    updatedSubjects[editIndex] = { name: newSubject, teacher, schedule };
    setSubjects(updatedSubjects);
    setNewSubject('');
    setTeacher('');
    setSchedule('');
    setEditIndex(null);
    setError('');
  };

  const handleDeleteSubject = (index) => {
    const filteredSubjects = subjects.filter((_, i) => i !== index);
    setSubjects(filteredSubjects);
  };

  return (
    <div className="subjects-crud-container">
      <Menu />
      <h1>Gestión de Materias</h1>
      <div className="form">
        <input
          type="text"
          placeholder="Nombre de la Materia"
          value={newSubject}
          onChange={(e) => setNewSubject(e.target.value)}
        />
        <input
          type="text"
          placeholder="Nombre del Profesor"
          value={teacher}
          onChange={(e) => setTeacher(e.target.value)}
        />
        <input
          type="text"
          placeholder="Horario"
          value={schedule}
          onChange={(e) => setSchedule(e.target.value)}
        />
        {editIndex !== null ? (
          <button onClick={handleSaveEdit}>Guardar</button>
        ) : (
          <button onClick={handleAddSubject}>Agregar Materia</button>
        )}
        {error && <p className="error">{error}</p>}
      </div>
      <ul className="subjects-list">
        {subjects.map((subject, index) => (
          <li key={index}>
            <span>Materia: {subject.name}</span>
            <span>Profesor: {subject.teacher}</span>
            <span>Horario: {subject.schedule}</span>
            <div className="actions">
              <button onClick={() => handleEditSubject(index)}>Editar</button>
              <button onClick={() => handleDeleteSubject(index)}>Eliminar</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SubjectsCRUD;
