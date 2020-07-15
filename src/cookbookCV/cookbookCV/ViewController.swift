//
//  ViewController.swift
//  cookbookCV
//
//  Created by Shrey Jain on 7/15/20.
//  Copyright © 2020 Shrey Jain. All rights reserved.
//

import UIKit
import Alamofire

class ViewController: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
    var imagePicker: UIImagePickerController!
    let url = "https://localhost:3000/"
    
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    @IBAction func takePhoto(_ sender: Any) {
        imagePicker = UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.sourceType = .camera
        present(imagePicker, animated: true, completion: nil)
    }
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        imagePicker.dismiss(animated: true, completion: nil)
        imageView.image = info[.originalImage] as? UIImage
    }
    
    @IBAction func uploadPhoto(_ sender: Any) {
        let image = imageView.image
        let imgData = image!.jpegData(compressionQuality: 0.2)!
        
        AF.upload(multipartFormData: { MultipartFormData in imgData

             MultipartFormData.append(imgData, withName: "image" , fileName: "image.jpeg" , mimeType: "image/jpeg")
                }, to: url, method: .post)
           .responseJSON { (response) in
                    debugPrint("SUCCESS RESPONSE: \(response)")
           }
        }
    }

