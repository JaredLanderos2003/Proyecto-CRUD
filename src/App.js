import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import SplashScreen from './components/SplashScreen';
import Welcome from './components/Welcome';
import Login from './components/Login';
import StudentsCRUD from './components/StudentsCRUD';
import SubjectsCRUD from './components/SubjectsCRUD';
import Enrollment from './components/Enrollment';
import GradesCapture from './components/Grades'; // Cambié el nombre del componente a GradesCapture
import Menu from './components/Menu';
import './App.css';

// Importa los contextos
import { StudentsProvider } from './context/StudentsContext';
import { SubjectsProvider } from './context/SubjectsContext';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    // Proveemos el contexto de estudiantes y materias
    <StudentsProvider>
      <SubjectsProvider>
        <Router>
          <div className="app">
            {isLoggedIn && <Menu onLogout={handleLogout} />}
            <Routes>
              <Route path="/" element={isLoggedIn ? <Navigate to="/welcome" /> : <Navigate to="/login" />} />
              <Route path="/login" element={!isLoggedIn ? <Login onLogin={handleLogin} /> : <Navigate to="/welcome" />} />
              <Route path="/welcome" element={isLoggedIn ? <Welcome /> : <Navigate to="/login" />} />
              {isLoggedIn && (
                <>
                  <Route path="/students" element={<StudentsCRUD />} />
                  <Route path="/subjects" element={<SubjectsCRUD />} />
                  <Route path="/enrollments" element={<Enrollment />} />
                  <Route path="/grades" element={<GradesCapture />} /> {/* Asegúrate de usar GradesCapture */}
                </>
              )}
            </Routes>
          </div>
        </Router>
      </SubjectsProvider>
    </StudentsProvider>
  );
}

export default App;
