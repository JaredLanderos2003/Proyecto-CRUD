import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    if (username === 'admin') {
      onLogin();
      navigate('/'); // Redirige a la vista de bienvenida después del login
    } else {
      alert('Credenciales incorrectas');
    }
  };

  return (
    <div className="login-container">
      {/* Usar la ruta pública para acceder a la imagen */}
      <img src="/i1.png" alt="EduManage Logo" className="login-logo" />
      <h2 className='texto1'>Control Escolar</h2>
      <h3>Login</h3>
      <input
        type="email"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button onClick={handleLogin}>Iniciar Sesión</button>
    </div>
  );
};

export default Login;
