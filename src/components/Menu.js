import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Menu.css';

const Menu = ({ onLogout }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);  // Controla la visibilidad del menú
  const navigate = useNavigate();

  // Función para alternar la visibilidad del menú
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  // Función para manejar el cierre de sesión
  const handleLogout = () => {
    // Llama la función onLogout que recibes desde el componente principal
    if (onLogout) {
      onLogout();  // Cambia el estado isLoggedIn en el componente principal a false
      navigate('/login');  // Redirige al login
    } else {
      console.error("onLogout no está definida como función");
    }
  };

  return (
    <div className="menu-container">
      <button className="menu-icon" onClick={toggleMenu}>
        ☰  {/* Ícono de menú */}
      </button>
      <div className={`menu-items ${isMenuOpen ? 'open' : ''}`}>
        <Link to="/students">Gestionar Alumnos</Link>
        <Link to="/subjects">Gestionar Materias</Link>
        <Link to="/enrollments">Inscripción</Link>
        <Link to="/grades">Captura de Calificaciones</Link>
        <Link to="/welcome">Inicio</Link>
        <button onClick={handleLogout}>Log Out</button> {/* Cerrar sesión */}
      </div>
    </div>
  );
};

export default Menu;
