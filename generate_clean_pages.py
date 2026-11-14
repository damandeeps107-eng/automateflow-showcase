#!/usr/bin/env python3
"""
Clean, High-End Redesign for:
1. Nexus Outlet Interior & Exterior (Mohali)
2. Shivaye Associates (Delhi NCR)

Aesthetic:
- Clean, crisp, white / warm ivory background (ZERO neon, ZERO dark gimmicks)
- Prominent real architectural photography in the hero banner
- Bold, legible typography (Poppins / Plus Jakarta Sans + Playfair / Fraunces)
- Elegant cards with subtle clean borders and warm accents
- Direct WhatsApp, call buttons, and interactive calculators
"""

def generate_clean_nexus():
    return """<!doctype html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nexus Outlet | Turnkey Interior &amp; Exterior Architecture Mohali</title>
  <meta name="description" content="Nexus Outlet Mohali - Turnkey luxury interiors, WPC exterior louvers, bespoke modular kitchens and charcoal wall panels in Sector 82 JLPL Mohali.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #FFFFFF;
      color: #1F2937;
      line-height: 1.6;
    }
    .font-serif-luxury {
      font-family: 'Playfair Display', Georgia, serif;
    }
    .top-bar-bg {
      background-color: #1E293B;
    }
    .hero-card-bg {
      background-color: #2D3748;
    }
    .btn-wa-green {
      background-color: #15803D;
      color: #FFFFFF;
      transition: all 0.2s ease;
    }
    .btn-wa-green:hover {
      background-color: #166534;
      transform: translateY(-2px);
      box-shadow: 0 10px 20px -5px rgba(21, 128, 61, 0.3);
    }
    .btn-dark {
      background-color: #1E293B;
      color: #FFFFFF;
      transition: all 0.2s ease;
    }
    .btn-dark:hover {
      background-color: #0F172A;
      transform: translateY(-2px);
    }
  </style>
</head>
<body class="selection:bg-amber-100 selection:text-amber-900">

  <!-- Top Announcement Bar -->
  <div class="top-bar-bg text-white text-xs py-2 px-4 border-b border-slate-700">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center space-x-2">
        <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="font-medium">Direct Factory Showroom:</span>
        <span class="text-slate-300">Plot 1559, Sector 82, JLPL Industrial Area, Mohali</span>
      </div>
      <div class="flex items-center space-x-6 text-slate-300">
        <span>⭐ 450+ Projects Handed Over</span>
        <a href="tel:+919914685221" class="text-amber-300 font-bold hover:underline">📞 +91 99146 85221</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center font-black text-amber-400 text-xl tracking-wider shadow-sm">
          NO
        </div>
        <div>
          <span class="text-2xl font-black tracking-tight text-slate-900">NEXUS OUTLET</span>
          <p class="text-[11px] font-semibold text-amber-600 uppercase tracking-wider">Interior &amp; Exterior Solutions • Mohali</p>
        </div>
      </div>

      <nav class="hidden md:flex items-center space-x-8 text-sm font-semibold text-slate-700">
        <a href="#projects" class="hover:text-amber-600 transition">Recent Work</a>
        <a href="#materials" class="hover:text-amber-600 transition">Materials &amp; Louvers</a>
        <a href="#calculator" class="hover:text-amber-600 transition">Cost Estimator</a>
        <a href="#showroom" class="hover:text-amber-600 transition">Showroom Location</a>
      </nav>

      <div class="flex items-center space-x-3">
        <a href="https://wa.me/919914685221?text=Hi%20Nexus%20Outlet%2C%20I%20am%20looking%20for%20interior%20%2F%20exterior%20work%20in%20Tricity." target="_blank" class="btn-wa-green px-4 py-2.5 rounded-lg text-xs sm:text-sm font-bold flex items-center gap-2 shadow-sm">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span>Chat on WhatsApp</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Clean Signature Hero Section (With Prominent Photo & High-End Card) -->
  <section class="bg-[#F8FAFC] py-12 sm:py-16 border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <!-- Left Hero Text & Booking Box -->
        <div class="lg:col-span-6 space-y-6">
          <div class="inline-flex items-center space-x-2 bg-amber-100 border border-amber-300 px-3.5 py-1.5 rounded-full text-xs font-bold text-amber-900">
            <span>✨ Turnkey Execution &amp; Wholesaler Pricing</span>
          </div>

          <h1 class="text-3xl sm:text-5xl font-extrabold text-slate-900 leading-tight">
            Luxury Residential Interiors &amp; <br>
            <span class="text-amber-600 font-serif-luxury italic">Exterior WPC Louver Facades</span>
          </h1>

          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
            Planning a new flat, luxury kothi, or commercial space in Mohali, Chandigarh or Zirakpur? Get direct wholesaler rates on WPC exterior louvers, turnkey living rooms, acrylic modular kitchens, and fluted charcoal panels.
          </p>

          <!-- Free Site Visit Card -->
          <div class="bg-white p-5 rounded-xl border border-gray-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between border-b border-gray-100 pb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-slate-700">Direct Consultation with Kiran Ji</span>
              <span class="text-xs text-emerald-600 font-bold">● Free Site Visit Available</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-600">
              <div class="flex items-center gap-2">✓ 100% In-House Material Supply</div>
              <div class="flex items-center gap-2">✓ 3D Layout &amp; Transparent BOM</div>
              <div class="flex items-center gap-2">✓ 10-Year Quality Guarantee</div>
              <div class="flex items-center gap-2">✓ 45-Day Handover Assurance</div>
            </div>
            <div class="pt-2 flex flex-wrap gap-3">
              <a href="https://wa.me/919914685221?text=Hi%20Kiran%20ji%2C%20I%20want%20to%20book%20a%20free%20site%20visit%20for%20my%20property." target="_blank" class="btn-wa-green px-5 py-3 rounded-lg font-bold text-xs flex items-center gap-2">
                <span>Book Free Site Visit on WhatsApp</span>
                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
              </a>
              <a href="tel:+919914685221" class="btn-dark px-5 py-3 rounded-lg font-bold text-xs flex items-center gap-2">
                <span>Call +91 99146 85221</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Right Large Hero Architectural Image -->
        <div class="lg:col-span-6">
          <div class="relative rounded-2xl overflow-hidden shadow-xl border border-gray-200">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85" alt="Nexus Outlet Architectural Villa Facade & Living" class="w-full h-[440px] object-cover">
            <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-4 rounded-xl border border-gray-100 flex items-center justify-between">
              <div>
                <p class="text-xs font-bold text-slate-900">Villa Elevation &amp; Exterior Louver Work</p>
                <p class="text-[11px] text-slate-500">Delivered in Sector 88, Mohali (Turnkey Execution)</p>
              </div>
              <span class="text-xs font-bold text-amber-700 bg-amber-50 px-2.5 py-1 rounded border border-amber-200">Recent Project</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Curated Work & Portfolio -->
  <section id="projects" class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <span class="text-xs uppercase font-bold tracking-widest text-amber-600">Real Handover Portfolio</span>
          <h2 class="text-3xl font-extrabold text-slate-900 mt-1">Our Recent Projects in Chandigarh Tricity</h2>
        </div>
        <p class="text-sm text-slate-500 max-w-md">
          Every project is backed by our direct Sector 82 manufacturing inventory and precision installation team.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Project 1: WPC Louvers -->
        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80" alt="WPC Louvers" class="w-full h-56 object-cover">
          <div class="p-5 space-y-3">
            <span class="text-[11px] font-bold uppercase text-amber-700 bg-amber-50 px-2.5 py-1 rounded">Exterior Elevation</span>
            <h3 class="text-base font-bold text-slate-900">WPC Exterior Louvers &amp; Weatherproof Cladding</h3>
            <p class="text-xs text-slate-600">UV-resistant, zero-maintenance exterior panels for modern kothis, bungalows and luxury commercial storefronts.</p>
            <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span class="text-xs text-slate-500">Sector 88 Mohali</span>
              <a href="https://wa.me/919914685221?text=Hi%20Nexus%20Outlet%2C%20Please%20share%20catalogue%20for%20WPC%20Louvers." target="_blank" class="text-xs font-bold text-amber-700 hover:underline">Get Price &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Project 2: Living Lounge -->
        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80" alt="Living Lounge" class="w-full h-56 object-cover">
          <div class="p-5 space-y-3">
            <span class="text-[11px] font-bold uppercase text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded">Turnkey Living</span>
            <h3 class="text-base font-bold text-slate-900">Charcoal Wall Louvers &amp; TV Console Paneling</h3>
            <p class="text-xs text-slate-600">Italian marble textures, concealed warm ambient LED cove lights, and fluted acoustic wall panels.</p>
            <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span class="text-xs text-slate-500">Aerocity Mohali</span>
              <a href="https://wa.me/919914685221?text=Hi%20Nexus%20Outlet%2C%20Please%20share%20cost%20estimate%20for%20TV%20Wall%20Paneling." target="_blank" class="text-xs font-bold text-amber-700 hover:underline">Get Price &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Project 3: Modular Kitchen -->
        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
          <img src="https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80" alt="Modular Kitchen" class="w-full h-56 object-cover">
          <div class="p-5 space-y-3">
            <span class="text-[11px] font-bold uppercase text-blue-700 bg-blue-50 px-2.5 py-1 rounded">Modular Kitchen</span>
            <h3 class="text-base font-bold text-slate-900">Acrylic Finish Island Modular Kitchen</h3>
            <p class="text-xs text-slate-600">Scratch-proof acrylic shutters, German soft-close tandem drawers, quartz countertops and pull-out tall unit.</p>
            <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span class="text-xs text-slate-500">Sector 70 Mohali</span>
              <a href="https://wa.me/919914685221?text=Hi%20Nexus%20Outlet%2C%20Please%20share%20modular%20kitchen%20quotation." target="_blank" class="text-xs font-bold text-amber-700 hover:underline">Get Price &rarr;</a>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Interactive Cost Estimator -->
  <section id="calculator" class="py-16 bg-[#F8FAFC] border-t border-b border-gray-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-10 space-y-2">
        <span class="text-xs uppercase font-bold tracking-widest text-amber-600">Transparent Budgeting</span>
        <h2 class="text-3xl font-extrabold text-slate-900">Instant Interior &amp; Exterior Cost Estimator</h2>
        <p class="text-xs sm:text-sm text-slate-500">Calculate budget estimate based on your space configuration in Mohali / Tricity.</p>
      </div>

      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200 space-y-6">
        <div>
          <label class="block text-xs font-bold uppercase text-slate-700 mb-2">1. Select Requirement</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <button onclick="calcNexus(1200, this)" class="n-btn py-3 px-3 rounded-lg border border-gray-200 text-xs font-semibold text-slate-700 hover:border-amber-600">2 BHK Flat</button>
            <button onclick="calcNexus(1800, this)" class="n-btn active-n py-3 px-3 rounded-lg border-2 border-amber-600 bg-amber-50 text-xs font-bold text-amber-900">3 BHK Flat</button>
            <button onclick="calcNexus(2800, this)" class="n-btn py-3 px-3 rounded-lg border border-gray-200 text-xs font-semibold text-slate-700 hover:border-amber-600">4 BHK / Kothi</button>
            <button onclick="calcNexus(800, this)" class="n-btn py-3 px-3 rounded-lg border border-gray-200 text-xs font-semibold text-slate-700 hover:border-amber-600">Exterior Facade Only</button>
          </div>
        </div>

        <div class="bg-slate-900 text-white p-6 rounded-xl flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <span class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Estimated Price Range</span>
            <div id="nexus_est" class="text-3xl font-extrabold text-amber-400 mt-1">₹6.5 - ₹8.5 Lakhs*</div>
            <p class="text-[11px] text-slate-400 mt-1">*Turnkey estimate including materials &amp; professional site installation.</p>
          </div>
          <button onclick="sendNexusWA()" class="btn-wa-green px-6 py-3 rounded-lg font-bold text-xs sm:text-sm flex items-center gap-2">
            <span>Get WhatsApp Quotation</span>
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          </button>
        </div>
      </div>

    </div>
  </section>

  <!-- Showroom Location -->
  <section id="showroom" class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-[#F8FAFC] rounded-2xl p-8 border border-gray-200">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
          <div class="space-y-4">
            <span class="text-xs uppercase font-bold text-amber-600">Experience Centre</span>
            <h3 class="text-2xl font-extrabold text-slate-900">Visit Our Mohali Factory Outlet</h3>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              Touch and feel real WPC exterior panels, charcoal louvers, and modular kitchen hardware in person.
            </p>
            <div class="text-xs space-y-2 text-slate-700">
              <p>📍 <strong>Address:</strong> Plot No. 1559, Sector 82, JLPL Industrial Area, Mohali (SAS Nagar), Punjab – 140308</p>
              <p>📞 <strong>Direct Contact:</strong> +91 99146 85221 (Kiran Aggarwal)</p>
              <p>⏰ <strong>Timings:</strong> 10:00 AM – 8:00 PM (Monday to Sunday)</p>
            </div>
            <div class="pt-2">
              <a href="https://maps.google.com/?q=Sector+82+JLPL+Industrial+Area+Mohali" target="_blank" class="inline-flex items-center gap-2 bg-slate-900 text-white text-xs font-bold px-4 py-2.5 rounded-lg hover:bg-slate-800 transition">
                <span>Open in Google Maps</span>
              </a>
            </div>
          </div>
          <div class="h-64 rounded-xl overflow-hidden border border-gray-300">
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13726.069796011326!2d76.7118!3d30.6756!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390fecc852a392ab%3A0xe54dcf9c48873f15!2sSector%2082%2C%20JLPL%20Industrial%20Area%2C%20Sahibzada%20Ajit%20Singh%20Nagar%2C%20Punjab%20140308!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" 
              class="w-full h-full border-0" 
              allowfullscreen="" 
              loading="lazy">
            </iframe>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Clean Footer -->
  <footer class="bg-slate-900 text-slate-400 text-xs py-10 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <p class="text-white font-bold text-sm">NEXUS OUTLET INTERIOR &amp; EXTERIOR</p>
        <p class="text-slate-400 mt-1">Plot 1559, Sector 82, JLPL Industrial Area, Mohali • +91 99146 85221</p>
      </div>
      <div class="text-slate-400">
        <span>Turnkey Residential &amp; Commercial Solutions</span>
      </div>
    </div>
  </footer>

  <script>
    let nSqft = 1800;
    function calcNexus(sqft, btn) {
      document.querySelectorAll('.n-btn').forEach(b => {
        b.className = 'n-btn py-3 px-3 rounded-lg border border-gray-200 text-xs font-semibold text-slate-700 hover:border-amber-600';
      });
      btn.className = 'n-btn active-n py-3 px-3 rounded-lg border-2 border-amber-600 bg-amber-50 text-xs font-bold text-amber-900';
      nSqft = sqft;
      let minL = Math.round(sqft * 350 / 100000 * 10) / 10;
      let maxL = Math.round(sqft * 500 / 100000 * 10) / 10;
      document.getElementById('nexus_est').innerText = '₹' + minL + ' - ₹' + maxL + ' Lakhs*';
    }
    function sendNexusWA() {
      let txt = 'Hi Nexus Outlet! I checked the cost estimator for ' + nSqft + ' sq. ft. space on your website. Please share detailed quotation.';
      window.open('https://wa.me/919914685221?text=' + encodeURIComponent(txt), '_blank');
    }
  </script>

</body>
</html>"""


def generate_clean_shivaye():
    return """<!doctype html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shivaye Associates | Luxury Builder Floors in West Delhi &amp; Dwarka Mor</title>
  <meta name="description" content="Shivaye Associates - Verified 2 BHK & 3 BHK luxury builder floors in Dwarka Mor, Uttam Nagar and West Delhi. Lift, Car Parking, Modular Kitchen & 90% Bank Loan Approved.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #FFFFFF;
      color: #1F2937;
      line-height: 1.6;
    }
    .top-navy {
      background-color: #0F172A;
    }
    .btn-wa-green {
      background-color: #15803D;
      color: #FFFFFF;
      transition: all 0.2s ease;
    }
    .btn-wa-green:hover {
      background-color: #166534;
      transform: translateY(-2px);
      box-shadow: 0 10px 20px -5px rgba(21, 128, 61, 0.3);
    }
    .btn-navy {
      background-color: #0F172A;
      color: #FFFFFF;
      transition: all 0.2s ease;
    }
    .btn-navy:hover {
      background-color: #1E293B;
      transform: translateY(-2px);
    }
    .prop-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      transition: all 0.25s ease;
    }
    .prop-card:hover {
      border-color: #CBD5E1;
      transform: translateY(-4px);
      box-shadow: 0 15px 30px -10px rgba(0, 0, 0, 0.08);
    }
  </style>
</head>
<body class="selection:bg-amber-100 selection:text-amber-900">

  <!-- Top Announcement Bar -->
  <div class="top-navy text-white text-xs py-2 px-4 border-b border-slate-800">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center space-x-2">
        <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="font-semibold text-amber-400">100% Freehold &amp; Registry Verified:</span>
        <span class="text-slate-300">Dwarka Mor &amp; Uttam Nagar Prime Metro Locations</span>
      </div>
      <div class="flex items-center space-x-6 text-slate-300">
        <span>🏦 Up to 90% Loan Available (SBI / HDFC)</span>
        <a href="tel:+919716793057" class="text-amber-400 font-bold hover:underline">📞 +91 97167 93057</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center font-black text-amber-400 text-xl tracking-wider shadow-sm">
          SA
        </div>
        <div>
          <span class="text-2xl font-black tracking-tight text-slate-900">SHIVAYE ASSOCIATES</span>
          <p class="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">Boutique Builder Floors • Delhi NCR</p>
        </div>
      </div>

      <nav class="hidden md:flex items-center space-x-8 text-sm font-semibold text-slate-700">
        <a href="#floors" class="hover:text-amber-600 transition">Builder Floors</a>
        <a href="#amenities" class="hover:text-amber-600 transition">Specifications</a>
        <a href="#calculator" class="hover:text-amber-600 transition">EMI Calculator</a>
        <a href="#contact" class="hover:text-amber-600 transition">Book Site Visit</a>
      </nav>

      <div class="flex items-center space-x-3">
        <a href="https://wa.me/919716793057?text=Hi%20Shivaye%20Associates%2C%20I%20am%20interested%20in%20a%202BHK%20%2F%203BHK%20builder%20floor%20visit." target="_blank" class="btn-wa-green px-4 py-2.5 rounded-lg text-xs sm:text-sm font-bold flex items-center gap-2 shadow-sm">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span>Chat on WhatsApp</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Clean Signature Hero Section with Real Property Photo -->
  <section class="bg-[#F8FAFC] py-12 sm:py-16 border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <!-- Left Hero Text & Site Visit Scheduler -->
        <div class="lg:col-span-6 space-y-6">
          <div class="inline-flex items-center space-x-2 bg-amber-100 border border-amber-300 px-3.5 py-1.5 rounded-full text-xs font-bold text-amber-900">
            <span>🏡 Direct Builder Mandate • 0% Brokerage</span>
          </div>

          <h1 class="text-3xl sm:text-5xl font-extrabold text-slate-900 leading-tight">
            Smart &amp; Luxurious <br>
            <span class="text-amber-700">Independent Builder Floors</span> <br>
            <span class="text-xl sm:text-2xl font-semibold text-slate-600">In Dwarka Mor &amp; Uttam Nagar, West Delhi</span>
          </h1>

          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
            Move into your ready dream home. Complete with branded elevator, covered stilt car parking, modern modular kitchen with chimney, 90% loan facility, and walking distance from Metro Station.
          </p>

          <!-- Free Site Visit Card -->
          <div class="bg-white p-5 rounded-xl border border-gray-200 shadow-sm space-y-3">
            <div class="flex items-center justify-between border-b border-gray-100 pb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-slate-800">Schedule A Free Site Tour</span>
              <span class="text-xs text-emerald-700 font-bold">● Metro Pick-up Available</span>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs text-slate-600">
              <div>✓ 100% Legal Title &amp; Registry</div>
              <div>✓ Direct Builder Pricing</div>
              <div>✓ Immediate Possession Ready</div>
              <div>✓ Bank Loan from SBI/HDFC/PNB</div>
            </div>
            <div class="pt-2 flex flex-wrap gap-3">
              <a href="https://wa.me/919716793057?text=Hi%20Shivaye%20Associates%2C%20Please%20schedule%20a%20site%20visit%20for%20a%20builder%20floor." target="_blank" class="btn-wa-green px-5 py-3 rounded-lg font-bold text-xs flex items-center gap-2">
                <span>Book Site Visit on WhatsApp</span>
                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
              </a>
              <a href="tel:+919716793057" class="btn-navy px-5 py-3 rounded-lg font-bold text-xs flex items-center gap-2">
                <span>Call +91 97167 93057</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Right Large Real Builder Floor Photo -->
        <div class="lg:col-span-6">
          <div class="relative rounded-2xl overflow-hidden shadow-xl border border-gray-200">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85" alt="Shivaye Associates Builder Floor Elevation & Living" class="w-full h-[440px] object-cover">
            <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-4 rounded-xl border border-gray-100 flex items-center justify-between">
              <div>
                <p class="text-xs font-bold text-slate-900">Luxury 2 &amp; 3 BHK Builder Floors with Lift &amp; Car Parking</p>
                <p class="text-[11px] text-slate-500">Dwarka Mor (300m from Metro) • Ready to Move</p>
              </div>
              <span class="text-xs font-bold text-amber-800 bg-amber-50 px-2.5 py-1 rounded border border-amber-300">₹28 Lakhs Onwards</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Curated Builder Floor Inventory -->
  <section id="floors" class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <span class="text-xs uppercase font-bold tracking-widest text-amber-700">Verified Units</span>
          <h2 class="text-3xl font-extrabold text-slate-900 mt-1">Available Ready &amp; Semi-Furnished Floors</h2>
        </div>
        <p class="text-sm text-slate-500 max-w-md">
          Zero hidden brokerage on direct builder floors. 100% transparent registration and bank loan assistance.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Floor 1: Smart 2 BHK -->
        <div class="prop-card rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80" alt="2 BHK Floor" class="w-full h-56 object-cover">
          <div class="p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-bold uppercase text-amber-800 bg-amber-50 px-2.5 py-1 rounded border border-amber-200">Smart 2 BHK</span>
              <span class="text-sm font-black text-slate-900">₹28 Lakhs*</span>
            </div>
            <h3 class="text-base font-bold text-slate-900">Independent 2 BHK with Lift &amp; Reserved Car Parking</h3>
            <p class="text-xs text-slate-600">📍 Dwarka Mor (300m from Metro Station). Includes modular kitchen, branded lift, LED false ceiling, and wide road access.</p>
            <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span class="text-xs text-emerald-700 font-semibold">90% Bank Loan Approved</span>
              <a href="https://wa.me/919716793057?text=Hi%20Shivaye%20Associates%2C%20Please%20share%202BHK%20Dwarka%20Mor%20floor%20plan%20and%20video." target="_blank" class="text-xs font-bold text-amber-700 hover:underline">Get Video &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Floor 2: Corner 3 BHK -->
        <div class="prop-card rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80" alt="3 BHK Floor" class="w-full h-56 object-cover">
          <div class="p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-bold uppercase text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded border border-emerald-200">Spacious 3 BHK</span>
              <span class="text-sm font-black text-slate-900">₹48 Lakhs*</span>
            </div>
            <h3 class="text-base font-bold text-slate-900">Two-Side Open Corner 3 BHK Independent Floor</h3>
            <p class="text-xs text-slate-600">📍 Uttam Nagar East / Janakpuri Border. Ample natural sunlight, Italian marble tiles, 2 luxury bathrooms with Jaguar fittings.</p>
            <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span class="text-xs text-emerald-700 font-semibold">Registry Ready</span>
              <a href="https://wa.me/919716793057?text=Hi%20Shivaye%20Associates%2C%20Please%20share%203BHK%20Corner%20Floor%20details." target="_blank" class="text-xs font-bold text-amber-700 hover:underline">Get Video &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Floor 3: Penthouse with Terrace -->
        <div class="prop-card rounded-xl overflow-hidden shadow-sm">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80" alt="Penthouse" class="w-full h-56 object-cover">
          <div class="p-5 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-bold uppercase text-purple-800 bg-purple-50 px-2.5 py-1 rounded border border-purple-200">Terrace Penthouse</span>
              <span class="text-sm font-black text-slate-900">₹65 Lakhs*</span>
            </div>
            <h3 class="text-base font-bold text-slate-900">3/4 BHK Floor with Exclusive Private Terrace Garden</h3>
            <p class="text-xs text-slate-600">📍 Near Metro Hub Dwarka Mor. Private terrace rights with gazebo setup, direct private elevator access, and double parking.</p>
            <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
              <span class="text-xs text-emerald-700 font-semibold">Exclusive Deal</span>
              <a href="https://wa.me/919716793057?text=Hi%20Shivaye%20Associates%2C%20Please%20share%20Terrace%20Penthouse%20details." target="_blank" class="text-xs font-bold text-amber-700 hover:underline">Get Video &rarr;</a>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Interactive Monthly EMI Calculator -->
  <section id="calculator" class="py-16 bg-[#F8FAFC] border-t border-b border-gray-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-10 space-y-2">
        <span class="text-xs uppercase font-bold tracking-widest text-amber-700">Financial Planning</span>
        <h2 class="text-3xl font-extrabold text-slate-900">Instant Monthly EMI Calculator</h2>
        <p class="text-xs sm:text-sm text-slate-500">Calculate how affordable your monthly home loan installment is.</p>
      </div>

      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200 space-y-6">
        <div>
          <div class="flex justify-between text-xs font-bold text-slate-700 mb-2">
            <span>Loan Amount Required</span>
            <span id="loan_num" class="text-amber-800 font-black text-base">₹30,00,000</span>
          </div>
          <input id="loan_range" type="range" min="1500000" max="8000000" step="100000" value="3000000" oninput="calcCleanEMI()" class="w-full accent-amber-700 cursor-pointer">
          <div class="flex justify-between text-[11px] text-slate-400 mt-1">
            <span>₹15 Lakhs</span>
            <span>₹50 Lakhs</span>
            <span>₹80 Lakhs</span>
          </div>
        </div>

        <div class="bg-slate-900 text-white p-6 rounded-xl flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <span class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Estimated Monthly EMI (20 Yrs @ 8.5%)</span>
            <div id="clean_emi" class="text-3xl font-extrabold text-amber-400 mt-1">₹26,035 / mo</div>
            <p class="text-[11px] text-slate-400 mt-1">*Eligible for Tax benefits under Section 80C &amp; 24b.</p>
          </div>
          <button onclick="sendShivayeWA()" class="btn-wa-green px-6 py-3 rounded-lg font-bold text-xs sm:text-sm flex items-center gap-2">
            <span>Check Bank Loan Eligibility</span>
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          </button>
        </div>
      </div>

    </div>
  </section>

  <!-- Clean Footer -->
  <footer id="contact" class="bg-slate-900 text-slate-400 text-xs py-10 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <p class="text-white font-bold text-sm">SHIVAYE ASSOCIATES</p>
        <p class="text-slate-400 mt-1">Dwarka Mor &amp; Uttam Nagar Hub, West Delhi • +91 97167 93057</p>
      </div>
      <div class="text-slate-400">
        <span>Verified Freehold Builder Floors &amp; Advisory</span>
      </div>
    </div>
  </footer>

  <script>
    function calcCleanEMI() {
      let p = parseFloat(document.getElementById('loan_range').value);
      document.getElementById('loan_num').innerText = '₹' + p.toLocaleString('en-IN');
      let n = 20 * 12;
      let r = 8.5 / 12 / 100;
      let emi = (p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
      document.getElementById('clean_emi').innerText = '₹' + Math.round(emi).toLocaleString('en-IN') + ' / mo';
    }
    function sendShivayeWA() {
      let p = document.getElementById('loan_range').value;
      let emi = document.getElementById('clean_emi').innerText;
      let txt = 'Hi Shivaye Associates! I calculated EMI on your website for ₹' + parseInt(p).toLocaleString('en-IN') + ' loan (' + emi + '). Please share available builder floor inventory and site visit timing.';
      window.open('https://wa.me/919716793057?text=' + encodeURIComponent(txt), '_blank');
    }
  </script>

</body>
</html>"""

with open('/Users/user/.gemini/antigravity/scratch/automateflow-showcase/nexus-outlet.html', 'w') as f:
    f.write(generate_clean_nexus())

with open('/Users/user/.gemini/antigravity/scratch/automateflow-showcase/shivaye-associates.html', 'w') as f:
    f.write(generate_clean_shivaye())

print("Both clean pages generated successfully!")
