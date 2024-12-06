import React, { createContext, useContext, useState } from 'react';

// Crear el contexto
const StudentsContext = createContext();

// Proveedor del contexto
export const StudentsProvider = ({ children }) => {
  const [students, setStudents] = useState([]);

  return (
    <StudentsContext.Provider value={{ students, setStudents }}>
      {children}
    </StudentsContext.Provider>
  );
};

// Hook personalizado para usar el contexto
export const useStudents = () => useContext(StudentsContext);
