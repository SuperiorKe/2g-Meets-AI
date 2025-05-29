
import React from 'react';

const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-dark text-gray-300 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p className="text-sm">
          &copy; {currentYear} SuperiaTech. All rights reserved.
        </p>
        <p className="text-xs mt-2">
          Empowering learning through accessible technology.
        </p>
        {/* <div className="mt-4 flex justify-center space-x-4">
          <a href="#" className="text-gray-400 hover:text-white transition-colors"><p>Privacy Policy</p></a>
          <a href="#" className="text-gray-400 hover:text-white transition-colors"><p>Terms of Service</p></a>
        </div> */}
      </div>
    </footer>
  );
};

export default Footer;
    