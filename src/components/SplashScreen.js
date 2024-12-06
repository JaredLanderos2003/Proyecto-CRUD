import React, { useEffect } from 'react';
import './SplashScreen.css';

const SplashScreen = ({ onFinish }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onFinish(); // Después de 3 segundos, redirige al login
    }, 3000);

    return () => clearTimeout(timer); // Limpia el temporizador si el componente se desmonta
  }, [onFinish]);

  return (
    <div className="splash-screen">
      <h1>Cargando...</h1>
    </div>
  );
};

export default SplashScreen;
