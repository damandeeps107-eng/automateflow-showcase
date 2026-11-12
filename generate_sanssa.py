import os

html_content = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sanssa Architecture &amp; Visuals | Ar. Gurpreet Singh • Mohali</title>
  <meta name="description" content="Sanssa Architecture & Visuals - Bespoke Modern Villa Architecture, Photorealistic 3D Visualizations, and Turnkey Site Execution in Mohali & Tricity. Led by Ar. Gurpreet Singh.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;1,400;1,600&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #0F172A;
      background-color: #FAFAFA;
      -webkit-font-smoothing: antialiased;
    }
    .font-serif-luxury {
      font-family: 'Playfair Display', Georgia, serif;
    }
    
    @keyframes heroEntrance {
      0% {
        opacity: 0.1;
        transform: translateY(14px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }
    .hero-container-anim {
      animation: heroEntrance 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .btn-wa-green {
      background-color: #25D366;
      color: #FFFFFF;
      transition: all 0.25s ease;
    }
    .btn-wa-green:hover {
      background-color: #1EBE5D;
      transform: translateY(-2px);
      box-shadow: 0 12px 24px -6px rgba(37, 211, 102, 0.45);
    }

    .glass-pill {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.22);
    }

    .floating-wa {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 99;
      box-shadow: 0 10px 25px rgba(37, 211, 102, 0.45);
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .floating-wa:hover {
      transform: scale(1.1) translateY(-3px);
    }

    @keyframes modalPop {
      0% {
        opacity: 0;
        transform: scale(0.95) translateY(10px);
      }
      100% {
        opacity: 1;
        transform: scale(1) translateY(0);
      }
    }
    .modal-box-anim {
      animation: modalPop 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
  </style>
</head>
<body class="selection:bg-amber-100 selection:text-amber-900">

  <!-- 1. Top Minimal Bar -->
  <div class="bg-[#0B1120] text-gray-300 text-[11px] sm:text-xs py-2 px-4 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex justify-between items-center gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="font-medium tracking-wide text-gray-200">SANSSA ARCHITECTURE &amp; 3D VISUALS • SECTOR 82 JLPL, MOHALI</span>
      </div>
      <div class="flex items-center gap-4 text-xs font-light">
        <span class="hidden md:inline">📍 Plot 1710, Sector 82, Mohali</span>
        <span class="hidden md:inline">•</span>
        <a href="tel:919041544437" class="hover:text-amber-400 text-gray-200 transition font-medium">📞 +91 90415 44437</a>
      </div>
    </div>
  </div>

  <!-- 2. Clean Minimal Header with Circular Logo -->
  <header class="bg-white/95 backdrop-blur-md border-b border-gray-100 sticky top-0 z-40 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 py-3 flex justify-between items-center">
      
      <!-- Brand with Circular Logo -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="w-11 h-11 sm:w-12 sm:h-12 rounded-full bg-[#0F172A] border-2 border-amber-500/50 flex items-center justify-center text-white shadow-md group-hover:scale-105 transition-transform flex-shrink-0">
          <span class="font-serif-luxury font-bold text-base sm:text-lg tracking-wider text-amber-400">SA</span>
        </div>
        <div>
          <span class="text-base sm:text-lg font-extrabold tracking-tight text-gray-900 block leading-tight">SANSSA ARCHITECTURE</span>
          <span class="text-[10px] sm:text-[11px] text-amber-700 font-semibold tracking-wider uppercase block">Ar. Gurpreet Singh • 3D Visuals &amp; Turnkey Execution</span>
        </div>
      </a>

      <!-- Quick Actions -->
      <div class="flex items-center gap-2 sm:gap-3">
        <button onclick="openInquiryModal('Header Consultation')" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold text-gray-700 bg-gray-50 border border-gray-200 px-3.5 py-2 rounded-full hover:bg-gray-100 transition">
          <svg class="w-3.5 h-3.5 text-amber-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          Call: 9041544437
        </button>
        <button onclick="openInquiryModal('Header WhatsApp')" class="btn-wa-green inline-flex items-center gap-1.5 text-xs font-semibold px-3.5 sm:px-4 py-2 rounded-full shadow-sm">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
          <span>WhatsApp Inquiry</span>
        </button>
      </div>

    </div>
  </header>

  <!-- 3. Minimal Ultra-Luxury Hero Section with Full-Bleed Architectural Image & Left-Aligned Text -->
  <section class="relative w-full min-h-[580px] sm:min-h-[660px] flex items-center bg-[#0B1120] overflow-hidden">
    
    <!-- Full-Bleed High-Res Architectural Background Image -->
    <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=2000&q=85" 
         alt="Sanssa Architecture Modern Villa Mohali" 
         class="absolute inset-0 w-full h-full object-cover object-center">

    <!-- Sophisticated Minimal Dark Gradient -->
    <div class="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/80 to-slate-950/30 sm:to-transparent"></div>
    <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-slate-950/40"></div>

    <!-- Left-Aligned Animated Text Container -->
    <div class="relative z-10 max-w-7xl mx-auto px-6 sm:px-12 w-full py-14 sm:py-20">
      <div class="max-w-xl text-white hero-container-anim">
        
        <!-- Badge -->
        <div class="inline-flex items-center gap-2 glass-pill px-3.5 py-1.5 rounded-full text-xs font-semibold text-amber-300 mb-4">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
          <span>Sector 82 JLPL Mohali • Turnkey Architecture</span>
        </div>

        <!-- Italic Script Line -->
        <p class="font-serif-luxury italic text-xl sm:text-2xl text-amber-200 mb-2 tracking-wide">
          Where 3D Vision Meets Precision Reality
        </p>

        <!-- Main Headline -->
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight leading-tight sm:leading-[1.15] mb-4 text-white">
          Modern Architecture &amp; Photorealistic 3D Visuals
        </h1>

        <!-- Subtitle -->
        <p class="text-gray-200 text-xs sm:text-base leading-relaxed mb-6 font-light max-w-lg">
          Led by Ar. Gurpreet Singh. Specializing in luxury villa elevations, structural blueprints, and 100% turnkey site execution across Mohali, Chandigarh &amp; Tricity.
        </p>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          <button onclick="openInquiryModal('Hero CTA - Consultation')" class="btn-wa-green inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full text-xs sm:text-sm font-semibold shadow-xl">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            <span>Book Architect Consultation</span>
          </button>
          <a href="#portfolio" class="glass-pill hover:bg-white/20 text-white px-5 py-3 rounded-full text-xs sm:text-sm font-medium transition flex items-center justify-center gap-2">
            <span>Explore 3D Portfolio ↓</span>
          </a>
        </div>

        <!-- Spec Pillars -->
        <div class="grid grid-cols-3 gap-4 pt-6 mt-8 border-t border-white/15 text-xs text-gray-300">
          <div>
            <span class="block text-amber-300 font-extrabold text-base sm:text-lg">100% Match</span>
            <span class="text-gray-300 font-normal">3D to Real Site</span>
          </div>
          <div>
            <span class="block text-amber-300 font-extrabold text-base sm:text-lg">Sector 82</span>
            <span class="text-gray-300 font-normal">JLPL Mohali Studio</span>
          </div>
          <div>
            <span class="block text-amber-300 font-extrabold text-base sm:text-lg">Turnkey</span>
            <span class="text-gray-300 font-normal">Concept to Handover</span>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 4. Featured Architectural Works -->
  <section id="portfolio" class="py-16 sm:py-20 max-w-7xl mx-auto px-4 sm:px-8">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-3">
      <div>
        <span class="text-amber-700 font-bold text-xs uppercase tracking-widest block mb-1">Portfolio Highlights</span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-gray-900 tracking-tight">3D Visualizations &amp; Handover Projects</h2>
      </div>
      <p class="text-gray-500 text-xs sm:text-sm max-w-md">
        Photorealistic 3D visualization backed by precise structural drawings and turnkey site execution.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
      
      <!-- Project 1 -->
      <div class="bg-white rounded-2xl overflow-hidden border border-gray-200/80 shadow-sm hover:shadow-xl transition-all duration-300 group">
        <div class="relative h-60 overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80" alt="Contemporary Courtyard Villa" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <div class="absolute top-3.5 left-3.5 bg-slate-900/90 backdrop-blur-md text-amber-300 text-[11px] font-bold px-3 py-1 rounded-full border border-amber-500/30">
            Completed Handover
          </div>
        </div>
        <div class="p-6">
          <span class="text-[11px] font-semibold text-amber-700 tracking-wider uppercase block mb-1">500 Sq. Yds. • Mohali Kothi</span>
          <h3 class="text-base sm:text-lg font-bold text-gray-900 mb-2">Contemporary Courtyard Villa</h3>
          <p class="text-gray-600 text-xs leading-relaxed mb-5 font-light">
            Double-height living lounge, cantilevered glass balconies, ambient facade linear lighting, and integrated internal green courtyard.
          </p>
          <button onclick="openInquiryModal('Contemporary Courtyard Villa (500 Sq. Yds.)')" class="btn-wa-green w-full py-2.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-2">
            <span>WhatsApp Project Details</span>
          </button>
        </div>
      </div>

      <!-- Project 2 -->
      <div class="bg-white rounded-2xl overflow-hidden border border-gray-200/80 shadow-sm hover:shadow-xl transition-all duration-300 group">
        <div class="relative h-60 overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80" alt="Bespoke Modern Elevation" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <div class="absolute top-3.5 left-3.5 bg-slate-900/90 backdrop-blur-md text-amber-300 text-[11px] font-bold px-3 py-1 rounded-full border border-amber-500/30">
            3D Photorealistic Render
          </div>
        </div>
        <div class="p-6">
          <span class="text-[11px] font-semibold text-amber-700 tracking-wider uppercase block mb-1">Wave Estate • Sector 85</span>
          <h3 class="text-base sm:text-lg font-bold text-gray-900 mb-2">Travertine &amp; Louver Elevation</h3>
          <p class="text-gray-600 text-xs leading-relaxed mb-5 font-light">
            Imported travertine stone cladding with vertical acoustic metal louvers, biophilic terrace deck, and private basement entertainment lounge.
          </p>
          <button onclick="openInquiryModal('Travertine & Louver Elevation (Wave Estate)')" class="btn-wa-green w-full py-2.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-2">
            <span>Get 3D Elevation Blueprint</span>
          </button>
        </div>
      </div>

      <!-- Project 3 -->
      <div class="bg-white rounded-2xl overflow-hidden border border-gray-200/80 shadow-sm hover:shadow-xl transition-all duration-300 group">
        <div class="relative h-60 overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80" alt="Turnkey Luxury Penthouse" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <div class="absolute top-3.5 left-3.5 bg-slate-900/90 backdrop-blur-md text-amber-300 text-[11px] font-bold px-3 py-1 rounded-full border border-amber-500/30">
            Bespoke Architecture
          </div>
        </div>
        <div class="p-6">
          <span class="text-[11px] font-semibold text-amber-700 tracking-wider uppercase block mb-1">Tricity Commercial / Studio</span>
          <h3 class="text-base sm:text-lg font-bold text-gray-900 mb-2">Minimalist Modern Penthouse</h3>
          <p class="text-gray-600 text-xs leading-relaxed mb-5 font-light">
            Monolithic exposed concrete aesthetics, seamless glass envelope, custom architectural joinery, and private plunge pool provision.
          </p>
          <button onclick="openInquiryModal('Minimalist Modern Penthouse Studio')" class="btn-wa-green w-full py-2.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-2">
            <span>WhatsApp Specifications</span>
          </button>
        </div>
      </div>

    </div>
  </section>

  <!-- 5. Minimal Trust Footprint -->
  <section class="bg-slate-900 text-white py-14 px-4 sm:px-8 border-t border-slate-800">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center sm:text-left">
      <div>
        <div class="flex items-center justify-center sm:justify-start gap-3 mb-3">
          <div class="w-8 h-8 rounded-full bg-slate-800 border border-amber-500/50 flex items-center justify-center text-amber-400 font-serif-luxury font-bold text-xs">
            SA
          </div>
          <span class="font-bold text-sm tracking-wide">SANSSA ARCHITECTURE</span>
        </div>
        <p class="text-gray-400 text-xs leading-relaxed max-w-sm">
          Specializing in 3D architectural visualization, luxury residential elevations, and end-to-end turnkey site execution across Punjab &amp; Tricity.
        </p>
      </div>
      <div>
        <span class="text-xs font-bold text-amber-400 tracking-wider uppercase block mb-2.5">Studio &amp; Consultations</span>
        <p class="text-gray-300 text-xs mb-1">📍 Plot 1710, Sector 82, JLPL Industrial Area, Mohali</p>
        <p class="text-gray-300 text-xs mb-1">📞 Direct: +91 90415 44437</p>
        <p class="text-gray-300 text-xs">💬 Instagram: @sanssa_visuals_mohali</p>
      </div>
      <div>
        <span class="text-xs font-bold text-amber-400 tracking-wider uppercase block mb-2.5">Studio Guarantee</span>
        <p class="text-gray-400 text-xs leading-relaxed">
          100% adherence from 3D conceptualization to actual on-site structural handover. Zero material discrepancies or hidden structural costs.
        </p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto mt-10 pt-6 border-t border-slate-800 text-center text-gray-500 text-[11px]">
      © 2026 Sanssa Architecture &amp; Visuals. All rights reserved. Ar. Gurpreet Singh.
    </div>
  </section>

  <!-- 6. Fixed Floating WhatsApp Button -->
  <button onclick="openInquiryModal('Floating WhatsApp Widget')" class="floating-wa w-14 h-14 bg-[#25D366] rounded-full flex items-center justify-center text-white" aria-label="WhatsApp Us">
    <svg class="w-8 h-8 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
  </button>

  <!-- 7. SMART ARCHITECTURAL LEAD POPUP -->
  <div id="inquiryModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/75 backdrop-blur-sm hidden">
    
    <div class="relative w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden border border-amber-500/30 modal-box-anim">
      
      <!-- Modal Header -->
      <div class="bg-gradient-to-r from-slate-950 to-slate-900 p-5 text-white flex items-center justify-between border-b border-amber-500/20">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-slate-800 border border-amber-400 flex items-center justify-center text-amber-400 font-serif-luxury font-bold text-sm">
            SA
          </div>
          <div>
            <h3 class="text-sm font-bold tracking-tight text-white leading-tight">Sanssa Architecture • Direct Inquiry</h3>
            <p class="text-[11px] text-amber-300 font-medium">Get 3D Blueprint &amp; Consultation on WhatsApp</p>
          </div>
        </div>
        <button onclick="closeInquiryModal()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 text-gray-300 hover:text-white flex items-center justify-center transition">
          ✕
        </button>
      </div>

      <!-- Modal Body -->
      <form id="leadForm" onsubmit="handleLeadSubmit(event)" class="p-6 space-y-4">
        <input type="hidden" id="inquirySource" value="Website Direct Popup">

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Aapka Naam / Full Name *</label>
          <input type="text" id="leadName" required placeholder="e.g. Gurmukh Singh" class="w-full px-3.5 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition">
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">WhatsApp Mobile Number *</label>
          <input type="tel" id="leadPhone" required pattern="[0-9]{10}" placeholder="10-digit mobile number" class="w-full px-3.5 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition">
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Project Type</label>
          <select id="leadProperty" class="w-full px-3.5 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl bg-white focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition">
            <option value="Luxury Villa Architecture & 3D Elevation">Luxury Villa Architecture & 3D Elevation</option>
            <option value="Turnkey Residential Construction & Execution">Turnkey Residential Construction & Execution</option>
            <option value="Commercial Landmark / Studio Design">Commercial Landmark / Studio Design</option>
            <option value="Interior 3D Visualization & Walkthrough">Interior 3D Visualization & Walkthrough</option>
          </select>
        </div>

        <div class="pt-2">
          <button type="submit" class="btn-wa-green w-full py-3.5 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 shadow-lg">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            <span>Send Project Inquiry to Ar. Gurpreet</span>
          </button>
        </div>

        <p class="text-[10px] text-gray-400 text-center">
          🔒 Aapki drawings aur project details 100% confidential rahengi.
        </p>
      </form>

    </div>
  </div>

  <script>
    function openInquiryModal(source) {
      if (source) {
        document.getElementById('inquirySource').value = source;
      }
      const modal = document.getElementById('inquiryModal');
      modal.classList.remove('hidden');
    }

    function closeInquiryModal() {
      const modal = document.getElementById('inquiryModal');
      modal.classList.add('hidden');
    }

    window.addEventListener('load', function() {
      setTimeout(function() {
        const modal = document.getElementById('inquiryModal');
        if (modal.classList.contains('hidden') && !sessionStorage.getItem('sanssa_modal_seen')) {
          openInquiryModal('Automated Welcome Popup');
          sessionStorage.setItem('sanssa_modal_seen', 'true');
        }
      }, 1800);
    });

    function handleLeadSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('leadName').value.trim();
      const phone = document.getElementById('leadPhone').value.trim();
      const property = document.getElementById('leadProperty').value;
      const source = document.getElementById('inquirySource').value;

      const text = encodeURIComponent(
        "Hi Ar. Gurpreet Singh & Sanssa Team,\\n" +
        "Maine aapki website se architectural project inquiry submit ki hai:\\n\\n" +
        "👤 Name: " + name + "\\n" +
        "📱 WhatsApp: +91 " + phone + "\\n" +
        "🏡 Project Type: " + property + "\\n" +
        "📍 Reference: " + source + "\\n\\n" +
        "Kripya 3D elevation samples aur project estimation details share karein."
      );

      const targetWaUrl = "https://wa.me/919041544437?text=" + text;
      closeInquiryModal();
      window.open(targetWaUrl, '_blank');
    }
  </script>

</body>
</html>
"""

with open('/Users/user/.gemini/antigravity/scratch/automateflow-showcase/sanssa-architecture.html', 'w') as f:
    f.write(html_content)

print("Generated sanssa-architecture.html successfully.")
