The project "RiftCo-Roadmap" is structured with a main directory named `rift-website`. Here's a summary of the contents and structure based on the files listed:

- **Configuration and Metadata:**
  - `.eslintrc.json`: Contains the linting rules for the project, ensuring code quality and consistency.
  - `package.json` & `package-lock.json`: Define the project dependencies and lock them to specific versions.
  - `next.config.js`: Configuration file for Next.js.
  - `postcss.config.js`: Configuration for PostCSS, a tool for transforming CSS with JavaScript.
  - `tailwind.config.ts`: Configuration for Tailwind CSS, a utility-first CSS framework.
  - `tsconfig.json`: Configuration for TypeScript, specifying the root files and compiler options.

- **Public Assets:**
  - `public/next.svg` & `public/vercel.svg`: SVG image assets, likely used within the application's UI.

- **Styling:**
  - `app/globals.css`: Global stylesheet for the application, defining universal CSS rules.

- **Core App Structure:**
  - `app/layout.tsx`: Likely defines the main layout of the application, including shared components like headers and footers.
  - `app/page.tsx`: Could be a template or a higher-order component for pages within the application.

- **Components:**
  - The `components` directory is organized into `footer`, `header`, and `roadmap` subdirectories, each containing React component files for their respective UI sections.
  - Examples include `additional_links.tsx`, `banner.tsx`, `main_nav.tsx`, and `title_section.tsx`, which suggest a structured and modular approach to the UI.

- **Documentation:**
  - `README.md`: The markdown file that usually contains instructions, project description, and other documentation.

- **Miscellaneous:**
  - `app/favicon.ico`: The website's favicon.

This structure indicates a typical Next.js application setup with a focus on a modular component architecture, leveraging modern web technologies like React, TypeScript, and Tailwind CSS.

Now, let's get the complete current structure of the project by querying the relevant files. Since the repository seems to be organized and not too large, I will query the content of the `README.md` file to provide more context about the project, as it often contains a summary or a description of the project's purpose and usage.

Let's proceed with that.

The `README.md` of the "RiftCo-Roadmap" project provides the following details:

- It's a [Next.js](https://nextjs.org/) project initialized with `create-next-app`.
- To get started, one can run the development server using npm, yarn, pnpm, or bun.
- The application is accessible at `http://localhost:3000` after starting the development server.
- The `app/page.tsx` is mentioned as the starting point for editing the application.
- The project uses `next/font` for font optimization, specifically for loading the Inter Google Font.


For a detailed view of the project, you can look at the `README.md` file in the repository: [README.md](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/README.md).

Here is the complete current structure of the project with links to each file in the repository:

- Configuration and Metadata:
  - [.eslintrc.json](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/.eslintrc.json)
  - [package.json](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/package.json)
  - [next.config.js](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/next.config.js)
  - [postcss.config.js](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/postcss.config.js)
  - [tailwind.config.ts](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/tailwind.config.ts)
  - [tsconfig.json](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/tsconfig.json)

- Public Assets:
  - [next.svg](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/public/next.svg)
  - [vercel.svg](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/public/vercel.svg)

- Styling:
  - [globals.css](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/app/globals.css)

- Core App Structure:
  - [layout.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/app/layout.tsx)
  - [page.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/app/page.tsx)

- Components:
  - Footer:
    - [additional_links.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/footer/additional_links.tsx)
    - [banner.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/footer/banner.tsx)
    - [copyrights.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/footer/copyrights.tsx)
    - [termsofservice.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/footer/termsofservice.tsx)
  - Header:
    - [about_link.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/header/about_link.tsx)
    - [contact_link.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/header/contact_link.tsx)
    - [home_link.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/header/home_link.tsx)
    - [main_nav.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/header/main_nav.tsx)
    - [products_menu.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/header/products_menu.tsx)
  - Roadmap:
    - [background_illustration.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/roadmap/background_illustration.tsx)
    - [milestones_icons.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/roadmap/milestones_icons.tsx)
    - [product_card/icon.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/roadmap/product_card/icon.tsx)
    - [product_card/label.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/roadmap/product_card/label.tsx)
    - [title_section.tsx](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/components/roadmap/title_section.tsx)

- Miscellaneous:
  - [favicon.ico](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/app/favicon.ico)

- Documentation:
  - [README.md](https://github.com/LucaCGN/RiftCo-Roadmap/blob/main/rift-website/README.md)

---
