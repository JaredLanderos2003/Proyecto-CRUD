import React, { createContext, useContext, useState, useEffect } from 'react';

const SubjectsContext = createContext();

export const useSubjects = () => useContext(SubjectsContext);

export const SubjectsProvider = ({ children }) => {
  // Carga inicial desde localStorage
  const [subjects, setSubjects] = useState(() => {
    const savedSubjects = localStorage.getItem('subjects');
    return savedSubjects ? JSON.parse(savedSubjects) : [];
  });

  // Sincroniza los datos con localStorage cada vez que cambian
  useEffect(() => {
    localStorage.setItem('subjects', JSON.stringify(subjects));
  }, [subjects]);

  return (
    <SubjectsContext.Provider value={{ subjects, setSubjects }}>
      {children}
    </SubjectsContext.Provider>
  );
};
