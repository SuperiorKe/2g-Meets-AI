import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Hero from './components/Hero';
import Features from './components/Features';
import HowItWorks from './components/HowItWorks';
import About from './components/About';
import Footer from './components/Footer';

const Home = () => (
  <>
    <Hero />
    <Features />
    <HowItWorks />
    <About />
  </>
);

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex min-h-screen flex-col bg-gray-50">
        <Header />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            {/* Add more routes as needed */}
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
    