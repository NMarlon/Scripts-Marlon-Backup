//  let sprite_sheet_path = "../sprites/MM_EXE1-3_overworld.png";
extern crate image;
extern crate sdl2;

use image::{DynamicImage, GenericImageView};
use sdl2::event::Event;
use sdl2::keyboard::Keycode;
use sdl2::pixels::PixelFormatEnum;
use sdl2::rect::Rect;
use sdl2::render::TextureCreator;
use sdl2::video::WindowContext;
use std::time::Duration;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Caminho para o sprite-sheet
    let sprite_sheet_path = "../sprites/MM_EXE1-3_overworld.png";

    // Carrega a imagem
    let sprite_sheet = image::open(sprite_sheet_path)?;

    // Dimensões de cada frame
    let frame_width = 32; // Largura do frame em pixels
    let frame_height = 32; // Altura do frame em pixels

    // Número de frames na sprite-sheet
    let num_frames_x = sprite_sheet.width() / frame_width;
    let num_frames_y = sprite_sheet.height() / frame_height;

    // Inicializa o SDL2
    let sdl_context = sdl2::init()?;
    let video_subsystem = sdl_context.video()?;
    let window = video_subsystem
        .window("Sprite Render", 800, 600)
        .position(0, 0)
        .build()?;
    let mut canvas = window.into_canvas().build()?;
    let texture_creator: TextureCreator<WindowContext> = canvas.texture_creator();

    let pixel_format = PixelFormatEnum::RGBA8888;

    let mut event_pump = sdl_context.event_pump()?;

    'mainloop: loop {
        for event in event_pump.poll_iter() {
            match event {
                Event::Quit { .. } | Event::KeyDown {
                    keycode: Some(Keycode::Escape),
                    ..
                } => break 'mainloop,
                _ => {}
            }
        }

        canvas.set_draw_color(sdl2::pixels::Color::RGBA(0, 0, 0, 0));
        canvas.clear();

        // Itera sobre os frames e desenha cada um na tela
        for y in 0..num_frames_y {
            for x in 0..num_frames_x {
                let frame = get_frame(&sprite_sheet, x * frame_width, y * frame_height, frame_width, frame_height);
                let mut texture = texture_creator.create_texture_streaming(pixel_format, frame.width(), frame.height())?;
                texture.update(None, frame.to_rgba().as_raw(), frame.width() as usize * 4)?;
                canvas.copy(&texture, None, Rect::new((x * frame_width) as i32, (y * frame_height) as i32, frame_width, frame_height))?;
            }
        }

        canvas.present();
        ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
    }

    Ok(())
}

fn get_frame(image: &DynamicImage, x: u32, y: u32, width: u32, height: u32) -> DynamicImage {
    // Cria um SubImage baseado nas coordenadas e dimensões e converte para DynamicImage
    DynamicImage::ImageRgba8(image.view(x, y, width, height).to_image())
}
