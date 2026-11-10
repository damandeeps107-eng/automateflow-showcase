#!/usr/bin/env python3
"""
Master Realtor / Property Advisory Landing Page Generator
Modern, Clean, Uncluttered Design with Poppins typography:
- Simple, modern, breathable layout (No serif/curly fonts)
- Clean header with brand logo & navigation
- Uncluttered hero section with prominent architectural photograph
- Curated luxury inventory collection with crisp modern cards
- Zero price mentions
"""

def generate_realtor_page(biz_name, handle, phone, city, logo_url, slug, properties=None):
    clean_handle = handle.replace("@", "").strip()
    
    if not properties:
        properties = [
            {
                "title": f"4 BHK Luxury Independent Floor",
                "tag": "Ready to Move",
                "specs": f"350–500 Sq. Yds. • {city}",
                "desc": "Spacious layout with private elevator access, covered stilt car parking, Italian marble living area, and expansive balconies.",
                "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": f"Signature Corner Penthouse",
                "tag": "Prime Location",
                "specs": f"500 Sq. Yds. • {city}",
                "desc": "Two-side open corner property with direct foyer elevator, open park views, modern modular kitchen, and private terrace.",
                "img": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": f"Executive 3 BHK Builder Floor",
                "tag": "Clear Registry",
                "specs": f"270–300 Sq. Yds. • {city}",
                "desc": "Prime connectivity near main sector roads. Gated security, 100% power backup, and ready for immediate registry.",
                "img": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=80"
            }
        ]

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{biz_name} | Prime Properties in {city}</title>
  <meta name="description" content="Verified luxury builder floors and properties in {city} by {biz_name}.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }}
    .btn-dark {{
      background-color: #0F172A;
      color: #FFFFFF;
      transition: all 0.2s ease;
    }}
    .btn-dark:hover {{
      background-color: #1E293B;
      transform: translateY(-1px);
    }}
    .btn-wa {{
      background-color: #16A34A;
      color: #FFFFFF;
      transition: all 0.2s ease;
    }}
    .btn-wa:hover {{
      background-color: #15803D;
      transform: translateY(-1px);
    }}
  </style>
</head>
<body class="selection:bg-slate-900 selection:text-white">

  <!-- Top Simple Strip -->
  <aside class="bg-slate-900 text-slate-300 py-2 px-4 text-center text-xs font-medium tracking-wide">
    Verified Direct Developer Inventory in {city} • Zero Middlemen
  </aside>

  <!-- Clean, Uncluttered Header -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Logo & Name -->
      <a href="#" class="flex items-center space-x-3">
        <img src="{logo_url}" alt="{biz_name}" class="w-11 h-11 rounded-full object-cover border border-slate-200 shadow-sm" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=200&q=80'">
        <div>
          <span class="text-base sm:text-lg font-semibold text-slate-900 block leading-tight">
            {biz_name}
          </span>
          <span class="text-xs text-slate-500 font-normal">
            Property Consultant • {city}
          </span>
        </div>
      </a>

      <!-- Simple Nav -->
      <nav class="hidden md:flex items-center space-x-8 text-xs font-medium text-slate-600">
        <a href="#properties" class="hover:text-slate-900 transition">Featured Inventory</a>
        <a href="#about" class="hover:text-slate-900 transition">Why Work With Us</a>
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-pink-600 transition flex items-center">
          Instagram: @{clean_handle}
        </a>
      </nav>

      <!-- Action Button -->
      <div>
        <a href="https://wa.me/{phone}?text=Hi%20{biz_name}%20Team,%20I%20am%20interested%20in%20viewing%20properties%20in%20{city}." class="btn-dark px-4 py-2.5 rounded-lg text-xs font-medium tracking-wide flex items-center">
          Schedule Walkthrough
        </a>
      </div>
    </div>
  </header>

  <!-- Clean Hero Section -->
  <main class="py-12 sm:py-16">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Hero Text (Clean & Simple) -->
      <div class="max-w-3xl mb-8">
        <span class="inline-block bg-slate-100 text-slate-700 text-xs font-semibold px-3 py-1 rounded-full mb-3">
          Direct Developer Mandate
        </span>
        <h1 class="text-3xl sm:text-5xl font-bold text-slate-900 tracking-tight leading-tight mb-4">
          Luxury Builder Floors &amp; Residences in {city}
        </h1>
        <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-normal">
          Explore ready-to-move and under-construction builder floors with clear titles, private elevator access, and prime sector connectivity.
        </p>
      </div>

      <!-- Prominent Clean Hero Image -->
      <div class="relative rounded-2xl overflow-hidden shadow-lg border border-slate-200 mb-12">
        <div class="aspect-[16/9] sm:aspect-[21/9] w-full bg-slate-900">
          <img 
            src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1800&q=85" 
            alt="Luxury Property Exterior" 
            class="w-full h-full object-cover"
          >
        </div>
        
        <!-- Simple Clean Overlay -->
        <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-transparent flex flex-col justify-end p-6 sm:p-8 text-white">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <span class="text-xs font-medium uppercase tracking-wider text-slate-300 block mb-1">
                Featured Inventory
              </span>
              <h2 class="text-lg sm:text-2xl font-semibold text-white">
                Independent Villa &amp; Floor Collections
              </h2>
            </div>
            <a href="https://wa.me/{phone}?text=Namaste%20{biz_name},%20please%20share%20walkthrough%20details." class="btn-wa px-5 py-2.5 rounded-lg text-xs font-semibold tracking-wide flex items-center">
              Watch Walkthrough on WhatsApp →
            </a>
          </div>
        </div>
      </div>

      <!-- 3 Clean Value Points -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-16">
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <div class="w-10 h-10 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-sm mb-3">01</div>
          <h3 class="text-base font-semibold text-slate-900 mb-1">100% Clear Titles</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Every property is verified for sanctioned maps, completion certificates, and smooth registry.
          </p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <div class="w-10 h-10 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold text-sm mb-3">02</div>
          <h3 class="text-base font-semibold text-slate-900 mb-1">Direct Developer Deals</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Get transparent builder payment terms and honest pricing without extra commission layers.
          </p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <div class="w-10 h-10 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center font-bold text-sm mb-3">03</div>
          <h3 class="text-base font-semibold text-slate-900 mb-1">Personalized Site Visits</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Schedule private property tours with dedicated on-ground assistance at your preferred time.
          </p>
        </div>
      </div>

      <!-- Properties Grid -->
      <div id="properties" class="pt-8">
        <div class="mb-8">
          <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider block mb-1">Available Portfolio</span>
          <h2 class="text-2xl font-bold text-slate-900">Current Available Units</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">"""

    for prop in properties:
        html += f"""
          <div class="bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm flex flex-col justify-between">
            <div>
              <div class="relative h-56 bg-slate-100 overflow-hidden">
                <img src="{prop['img']}" alt="{prop['title']}" class="w-full h-full object-cover">
                <span class="absolute top-3 left-3 bg-slate-900/80 text-white text-[11px] font-medium px-2.5 py-1 rounded">
                  {prop['tag']}
                </span>
              </div>
              <div class="p-5">
                <span class="text-xs font-medium text-slate-500 block mb-1">{prop['specs']}</span>
                <h3 class="text-base font-semibold text-slate-900 mb-2 leading-snug">{prop['title']}</h3>
                <p class="text-xs text-slate-600 leading-relaxed mb-4">{prop['desc']}</p>
              </div>
            </div>
            <div class="p-5 pt-0">
              <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20am%20interested%20in%20{prop['title']}.%20Please%20share%20details." class="w-full btn-dark py-2.5 rounded-lg text-xs font-medium text-center block">
                Inquire on WhatsApp →
              </a>
            </div>
          </div>"""

    html += f"""
        </div>
      </div>

    </div>
  </main>

  <!-- Clean Footer -->
  <footer class="border-t border-slate-200 bg-white py-10 text-xs text-slate-500">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <span class="font-semibold text-slate-900">{biz_name}</span> • Property Consultant in {city}
      </div>
      <div class="flex items-center space-x-6">
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-slate-900">Instagram: @{clean_handle}</a>
        <a href="https://wa.me/{phone}" class="text-emerald-600 font-medium hover:underline">WhatsApp: +{phone}</a>
      </div>
    </div>
  </footer>

</body>
</html>"""
    return html

if __name__ == "__main__":
    print("Clean Poppins Realtor Generator Loaded.")
