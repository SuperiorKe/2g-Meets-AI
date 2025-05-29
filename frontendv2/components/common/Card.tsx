
import React from 'react';

interface CardProps {
  icon?: React.ReactNode;
  title: string;
  description: string;
  className?: string;
}

const Card: React.FC<CardProps> = ({ icon, title, description, className = '' }) => {
  return (
    <div className={`bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 flex flex-col items-center text-center ${className}`}>
      {icon && <div className="mb-4 text-secondary">{icon}</div>}
      <h3 className="text-xl font-semibold text-primary mb-2">{title}</h3>
      <p className="text-gray-600 text-sm leading-relaxed">{description}</p>
    </div>
  );
};

export default Card;
    