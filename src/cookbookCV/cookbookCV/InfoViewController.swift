//
//  InfoViewController.swift
//  cookbookCV
//
//  Created by Shrey Jain on 8/5/20.
//  Copyright © 2020 Shrey Jain. All rights reserved.
//

import UIKit

class InfoViewController: UIViewController {

    @IBAction func shashankLinkedin(_ sender: Any) {
        if let url = URL(string: "https://www.linkedin.com/in/shashank-vemuri/") {
            UIApplication.shared.open(url)
        }
    }
    
    @IBAction func shreyLinkedin(_ sender: Any) {
        if let url = URL(string: "https://www.linkedin.com/in/shreypjain/") {
            UIApplication.shared.open(url)
        }
    }
    
    @IBAction func shreyaLinkedin(_ sender: Any) {
        if let url = URL(string: "https://www.linkedin.com/in/shreya-chaudhary-/") {
            UIApplication.shared.open(url)
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
