import os

html_content = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presto Estates | Luxury Builder Floors in DLF Phase 2, Gurgaon</title>
  <meta name="description" content="Presto Estates - Curated Luxury Independent Builder Floors and Distress Deals in DLF Phase 2, Gurugram. Direct builder mandate, private elevators, and prime connectivity to Cyber City.">
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
    
    /* Clean entrance animation */
    @keyframes heroEntrance {
      0% {
        opacity: 0.1;
        transform: translateY(12px);
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

    /* Modal Animation */
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
        <span class="font-medium tracking-wide text-gray-200">DLF PHASE 2 &amp; CYBER CITY • DIRECT BUILDER MANDATE</span>
      </div>
      <div class="flex items-center gap-4 text-xs font-light">
        <span class="hidden md:inline">📍 DLF Phase 2, Gurugram</span>
        <span class="hidden md:inline">•</span>
        <a href="tel:917424001000" class="hover:text-amber-400 text-gray-200 transition font-medium">📞 +91 7424001000</a>
      </div>
    </div>
  </div>

  <!-- 2. Clean Minimal Header with Original Circular Logo -->
  <header class="bg-white/95 backdrop-blur-md border-b border-gray-100 sticky top-0 z-40 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 py-3 flex justify-between items-center">
      
      <!-- Brand with Original Circular Logo -->
      <a href="#" class="flex items-center gap-3 group">
        <!-- Proper Circle Original Logo -->
        <div class="w-11 h-11 sm:w-12 sm:h-12 rounded-full overflow-hidden border-2 border-amber-500/60 shadow-md group-hover:scale-105 transition-transform flex-shrink-0 bg-slate-900">
          <img src="assets/presto_original_logo.png" alt="Presto Estates Official Logo" class="w-full h-full object-cover">
        </div>
        <div>
          <span class="text-base sm:text-lg font-extrabold tracking-tight text-gray-900 block leading-tight">PRESTO ESTATES</span>
          <span class="text-[10px] sm:text-[11px] text-amber-700 font-semibold tracking-wider uppercase block">Luxury Real Estate Advisory • DLF Gurgaon</span>
        </div>
      </a>

      <!-- Quick Actions -->
      <div class="flex items-center gap-2 sm:gap-3">
        <button onclick="openInquiryModal('Header Quick Inquiry')" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold text-gray-700 bg-gray-50 border border-gray-200 px-3.5 py-2 rounded-full hover:bg-gray-100 transition">
          <svg class="w-3.5 h-3.5 text-amber-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          Call: 7424001000
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
    
    <!-- Full-Bleed Architectural Luxury Image Background -->
    <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=2000&q=85" 
         alt="Luxury DLF Builder Floors Presto Estates" 
         class="absolute inset-0 w-full h-full object-cover object-center">

    <!-- Sophisticated Minimal Dark Gradient: Heavy on left for crisp readability, fades subtly to right -->
    <div class="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/80 to-slate-950/30 sm:to-transparent"></div>
    <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-slate-950/40"></div>

    <!-- Left-Aligned Animated Text Container -->
    <div class="relative z-10 max-w-7xl mx-auto px-6 sm:px-12 w-full py-14 sm:py-20">
      <div class="max-w-xl text-white hero-container-anim">
        
        <!-- Badge -->
        <div class="inline-flex items-center gap-2 glass-pill px-3.5 py-1.5 rounded-full text-xs font-semibold text-amber-300 mb-4">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
          <span>DLF Phase 2 &amp; Cyber City • Starting ₹3.50 Cr</span>
        </div>

        <!-- Italic Script Line -->
        <p class="font-serif-luxury italic text-xl sm:text-2xl text-amber-200 mb-2 tracking-wide">
          Distress Deals &amp; Bespoke Builder Floors
        </p>

        <!-- Main Headline -->
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight leading-tight sm:leading-[1.15] mb-4 text-white">
          Luxury Living in the Heart of DLF Gurgaon
        </h1>

        <!-- Subtitle -->
        <p class="text-gray-200 text-xs sm:text-base leading-relaxed mb-6 font-light max-w-lg">
          Curated 350 to 500 Sq. Yds. independent luxury builder floors in DLF Phase 2. Private high-speed elevator access, 3 covered car parks, Italian marble, and immediate connectivity to Cyber City &amp; MG Road.
        </p>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          <button onclick="openInquiryModal('Hero CTA - Verified Site Visit')" class="btn-wa-green inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full text-xs sm:text-sm font-semibold shadow-xl">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            <span>Book Verified Site Visit</span>
          </button>
          <a href="tel:917424001000" class="glass-pill hover:bg-white/20 text-white px-5 py-3 rounded-full text-xs sm:text-sm font-medium transition flex items-center justify-center gap-2">
            <span>📞 Call: 7424001000</span>
          </a>
        </div>

        <!-- Spec Pillars -->
        <div class="grid grid-cols-3 gap-4 pt-6 mt-8 border-t border-white/15 text-xs text-gray-300">
          <div>
            <span class="block text-amber-300 font-extrabold text-base sm:text-lg">₹3.50 Cr+</span>
            <span class="text-gray-300 font-normal">Starting Price</span>
          </div>
          <div>
            <span class="block text-amber-300 font-extrabold text-base sm:text-lg">DLF Ph-2</span>
            <span class="text-gray-300 font-normal">Prime Location</span>
          </div>
          <div>
            <span class="block text-amber-300 font-extrabold text-base sm:text-lg">100%</span>
            <span class="text-gray-300 font-normal">Direct Mandate</span>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 4. Featured Properties (Curated DLF Phase 2 Inventory) -->
  <section id="inventory" class="py-16 sm:py-20 max-w-7xl mx-auto px-4 sm:px-8">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-3">
      <div>
        <span class="text-amber-700 font-bold text-xs uppercase tracking-widest block mb-1">Curated Inventory</span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-gray-900 tracking-tight">Available Residences in DLF Phase 2</h2>
      </div>
      <p class="text-gray-500 text-xs sm:text-sm max-w-md">
        Direct builder mandates with verified registry documents and zero hidden commission disputes.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
      
      <!-- Card 1 -->
      <div class="bg-white rounded-2xl overflow-hidden border border-gray-200/80 shadow-sm hover:shadow-xl transition-all duration-300 group">
        <div class="relative h-60 overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80" alt="DLF Phase 2 Luxury Builder Floor" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <div class="absolute top-3.5 left-3.5 bg-slate-900/90 backdrop-blur-md text-amber-300 text-[11px] font-bold px-3 py-1 rounded-full border border-amber-500/30">
            Ready for Registry
          </div>
          <div class="absolute bottom-3.5 right-3.5 bg-white/95 text-slate-900 text-xs font-bold px-3 py-1 rounded-md shadow">
            ₹3.50 Cr Onwards
          </div>
        </div>
        <div class="p-6">
          <span class="text-[11px] font-semibold text-amber-700 tracking-wider uppercase block mb-1">350–500 Sq. Yds. • DLF Phase 2</span>
          <h3 class="text-base sm:text-lg font-bold text-gray-900 mb-2">Luxury Independent Builder Floor</h3>
          <p class="text-gray-600 text-xs leading-relaxed mb-5 font-light">
            Italian marble flooring, private elevator access directly into apartment foyer, 3 dedicated stilt car parks, premium modular kitchen, 2 mins from Cyber City.
          </p>
          <button onclick="openInquiryModal('DLF Phase 2 Luxury Builder Floor (₹3.50 Cr)')" class="btn-wa-green w-full py-2.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-2">
            <span>WhatsApp Floor Plan</span>
          </button>
        </div>
      </div>

      <!-- Card 2 (Distress Deal) -->
      <div class="bg-white rounded-2xl overflow-hidden border-2 border-amber-500/50 shadow-sm hover:shadow-xl transition-all duration-300 group relative">
        <div class="relative h-60 overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80" alt="Distress Deal DLF Gurgaon" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <div class="absolute top-3.5 left-3.5 bg-red-600 text-white text-[11px] font-bold px-3 py-1 rounded-full shadow">
            🔥 Exclusive Distress Deal
          </div>
          <div class="absolute bottom-3.5 right-3.5 bg-white/95 text-slate-900 text-xs font-bold px-3 py-1 rounded-md shadow">
            Below Market Value
          </div>
        </div>
        <div class="p-6">
          <span class="text-[11px] font-semibold text-amber-700 tracking-wider uppercase block mb-1">500 Sq. Yds. Corner • DLF Phase 2</span>
          <h3 class="text-base sm:text-lg font-bold text-gray-900 mb-2">Park-Facing Signature Floor</h3>
          <p class="text-gray-600 text-xs leading-relaxed mb-5 font-light">
            Double-height ceiling, bespoke terrace lounge, central VRV air conditioning, 100% power backup. High ROI potential for premium end-users &amp; property investors.
          </p>
          <button onclick="openInquiryModal('DLF Distress Deal (Park-Facing 500 Sq. Yds.)')" class="btn-wa-green w-full py-2.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-2">
            <span>Get Distress Deal Details</span>
          </button>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="bg-white rounded-2xl overflow-hidden border border-gray-200/80 shadow-sm hover:shadow-xl transition-all duration-300 group">
        <div class="relative h-60 overflow-hidden bg-gray-100">
          <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80" alt="Cyber City Facing Penthouse" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <div class="absolute top-3.5 left-3.5 bg-slate-900/90 backdrop-blur-md text-amber-300 text-[11px] font-bold px-3 py-1 rounded-full border border-amber-500/30">
            Private Terrace
          </div>
          <div class="absolute bottom-3.5 right-3.5 bg-white/95 text-slate-900 text-xs font-bold px-3 py-1 rounded-md shadow">
            4 BHK + Servant
          </div>
        </div>
        <div class="p-6">
          <span class="text-[11px] font-semibold text-amber-700 tracking-wider uppercase block mb-1">Luxury Penthouse • Gurugram</span>
          <h3 class="text-base sm:text-lg font-bold text-gray-900 mb-2">Executive Penthouse &amp; Terrace</h3>
          <p class="text-gray-600 text-xs leading-relaxed mb-5 font-light">
            Unobstructed skyline view, smart home automation, high-speed elevator, 4-tier security. Walking distance from MG Road &amp; Cyber Hub.
          </p>
          <button onclick="openInquiryModal('Cyber City Penthouse with Terrace')" class="btn-wa-green w-full py-2.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-2">
            <span>WhatsApp Penthouse Specs</span>
          </button>
        </div>
      </div>

    </div>
  </section>

  <!-- 5. Minimal Trust Footprint with Original Logo -->
  <section class="bg-slate-900 text-white py-14 px-4 sm:px-8 border-t border-slate-800">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center sm:text-left">
      <div>
        <div class="flex items-center justify-center sm:justify-start gap-3 mb-3">
          <div class="w-9 h-9 rounded-full overflow-hidden border border-amber-500/50 flex-shrink-0 bg-slate-950">
            <img src="assets/presto_original_logo.png" alt="Presto Estates Logo" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm tracking-wide">PRESTO ESTATES</span>
        </div>
        <p class="text-gray-400 text-xs leading-relaxed max-w-sm">
          Specialized in ultra-luxury builder floors and high-value distress transactions in DLF Phase 2, DLF Phase 1, and Golf Course Road, Gurugram.
        </p>
      </div>
      <div>
        <span class="text-xs font-bold text-amber-400 tracking-wider uppercase block mb-2.5">Contact &amp; Site Visits</span>
        <p class="text-gray-300 text-xs mb-1">📍 DLF Phase 2, Gurugram, Haryana</p>
        <p class="text-gray-300 text-xs mb-1">📞 Direct: +91 7424001000</p>
        <p class="text-gray-300 text-xs">💬 Instagram: @prestoestates</p>
      </div>
      <div>
        <span class="text-xs font-bold text-amber-400 tracking-wider uppercase block mb-2.5">Direct Mandate Assurance</span>
        <p class="text-gray-400 text-xs leading-relaxed">
          All properties verified with RERA approved sanction plans, structural warranties, and clear title documentation for high-net-worth buyers and investors.
        </p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto mt-10 pt-6 border-t border-slate-800 text-center text-gray-500 text-[11px]">
      © 2026 Presto Estates. All rights reserved. RERA Registered Real Estate Consultancy Gurugram.
    </div>
  </section>

  <!-- 6. Fixed Floating WhatsApp Button -->
  <button onclick="openInquiryModal('Floating WhatsApp Widget')" class="floating-wa w-14 h-14 bg-[#25D366] rounded-full flex items-center justify-center text-white" aria-label="WhatsApp Us">
    <svg class="w-8 h-8 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
  </button>

  <!-- 7. SMART LEAD CAPTURE POPUP (Direct WhatsApp Forwarding) -->
  <div id="inquiryModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/75 backdrop-blur-sm hidden">
    
    <div class="relative w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden border border-amber-500/30 modal-box-anim">
      
      <!-- Modal Header with Original Logo & Close Button -->
      <div class="bg-gradient-to-r from-slate-950 to-slate-900 p-5 text-white flex items-center justify-between border-b border-amber-500/20">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full overflow-hidden border border-amber-400 flex-shrink-0 bg-black">
            <img src="assets/presto_original_logo.png" alt="Presto Estates Logo" class="w-full h-full object-cover">
          </div>
          <div>
            <h3 class="text-sm font-bold tracking-tight text-white leading-tight">Presto Estates • Direct Inquiry</h3>
            <p class="text-[11px] text-amber-300 font-medium">Get Pricing &amp; Floor Plans on WhatsApp</p>
          </div>
        </div>
        <button onclick="closeInquiryModal()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 text-gray-300 hover:text-white flex items-center justify-center transition">
          ✕
        </button>
      </div>

      <!-- Modal Body (Input Form) -->
      <form id="leadForm" onsubmit="handleLeadSubmit(event)" class="p-6 space-y-4">
        <input type="hidden" id="inquirySource" value="Website Direct Popup">

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Aapka Naam / Full Name *</label>
          <input type="text" id="leadName" required placeholder="e.g. Rahul Sharma" class="w-full px-3.5 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition">
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">WhatsApp Mobile Number *</label>
          <input type="tel" id="leadPhone" required pattern="[0-9]{10}" placeholder="10-digit mobile number" class="w-full px-3.5 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition">
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Interested Property</label>
          <select id="leadProperty" class="w-full px-3.5 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl bg-white focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition">
            <option value="DLF Phase 2 Luxury Builder Floor (₹3.50 Cr+)">DLF Phase 2 Luxury Builder Floor (₹3.50 Cr+)</option>
            <option value="Exclusive Distress Deal in DLF Gurgaon">Exclusive Distress Deal in DLF Gurgaon</option>
            <option value="Cyber City Penthouse with Private Terrace">Cyber City Penthouse with Private Terrace</option>
            <option value="General Luxury Kothi / Independent Plot">General Luxury Kothi / Independent Plot</option>
          </select>
        </div>

        <div class="pt-2">
          <button type="submit" class="btn-wa-green w-full py-3.5 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 shadow-lg">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            <span>Send Inquiry Direct to Presto WhatsApp</span>
          </button>
        </div>

        <p class="text-[10px] text-gray-400 text-center">
          🔒 Aapki details 100% private rahengi. Presto Estates advisory team aapse direct connect karegi.
        </p>
      </form>

    </div>
  </div>

  <!-- Client-Side Script for Auto-Popup & Instant WhatsApp Submission -->
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

    // Auto-open modal after 1.8 seconds on page load
    window.addEventListener('load', function() {
      setTimeout(function() {
        // Only open if modal hasn't been closed
        const modal = document.getElementById('inquiryModal');
        if (modal.classList.contains('hidden') && !sessionStorage.getItem('presto_modal_seen')) {
          openInquiryModal('Automated Welcome Popup');
          sessionStorage.setItem('presto_modal_seen', 'true');
        }
      }, 1800);
    });

    // Handle Form Submit and forward directly to Presto Estates WhatsApp
    function handleLeadSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('leadName').value.trim();
      const phone = document.getElementById('leadPhone').value.trim();
      const property = document.getElementById('leadProperty').value;
      const source = document.getElementById('inquirySource').value;

      // Construct professional WhatsApp message
      const text = encodeURIComponent(
        "Hi Presto Estates Team,\\n" +
        "Maine aapki website se verified property inquiry submit ki hai:\\n\\n" +
        "👤 Name: " + name + "\\n" +
        "📱 WhatsApp: +91 " + phone + "\\n" +
        "🏡 Interested Property: " + property + "\\n" +
        "📍 Reference: " + source + "\\n\\n" +
        "Kripya floor plans aur verified pricing share karein."
      );

      const targetWaUrl = "https://wa.me/917424001000?text=" + text;
      
      // Close modal
      closeInquiryModal();

      // Redirect directly to WhatsApp
      window.open(targetWaUrl, '_blank');
    }
  </script>

</body>
</html>
"""

with open('/Users/user/.gemini/antigravity/scratch/automateflow-showcase/presto-estates.html', 'w') as f:
    f.write(html_content)

print("Generated presto-estates.html with official logo and direct WhatsApp popup.")
